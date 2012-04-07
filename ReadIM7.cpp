/* ReadIM7
	TL 05.01.04

	Read a LaVision IM7/VC7 file by a call to:

   int ReadIM7 ( const char* theFileName, BufferType* myBuffer, AttributeList** myList );

   If you don't want to read the attributes, set myList = NULL. If myList is set,
   the parameter returns a pointer to the list. You have to free the strings manually!

   The function returns the error codes of ImReadError_t.
*/

#include "ReadIMX.h"
#include "ReadIM7.h"
#include "zlib/zlib.h"

enum IM7PackType_t
{
	IM7_PACKTYPE__UNCOMPR= 0x1000,// autoselect uncompressed
	IM7_PACKTYPE__FAST,				// autoselect fastest packtype,
	IM7_PACKTYPE__SIZE,				// autoselect packtype with smallest resulting file
	IM7_PACKTYPE_IMG			= 0,	// uncompressed, like IMG
	IM7_PACKTYPE_IMX,					// old version compression, like IMX
	IM7_PACKTYPE_ZLIB,				// zlib
	IM7_PACKTYPE_FIXED_12_0,		// 12 bit format without bitshift
};


ImReadError_t SCPackUncompressed_Read( FILE* theFile, BufferType* myBuffer, bool p_bBytes )
{
	for (int row=0; row<myBuffer->totalLines; row++)
	{
		unsigned long destLen = 0;
		Byte *dest = Buffer_GetRowAddrAndSize(myBuffer,row,destLen);

		if (p_bBytes)
		{	// read row of bytes
			destLen /= 2;
			size_t n = fread(dest,1,destLen,theFile);
			if (n!=destLen || ferror(theFile))
				return IMREAD_ERR_DATA;
			// copy bytes into the words
			Word *pWord = (Word*)dest;
			for (int i=destLen-1; i>=0; i--)
				pWord[i] = dest[i];
		}
		else
		{	// read row of words
			size_t n = fread(dest,1,destLen,theFile);
			//fprintf(stderr,"%i %i %i\n",row,destLen,n);
			if (n!=destLen || ferror(theFile))
				return IMREAD_ERR_DATA;
		}
	}
	return IMREAD_ERR_NO;
}



ImReadError_t SCPackZlib_Read( FILE* theFile, BufferType* myBuffer )
{
	int sourceLen = 0;
	Bytef *source = NULL;

	fread( &sourceLen, sizeof(sourceLen), 1, theFile );
	//fprintf(stderr,"sourcelen: %i\n",sourceLen);
	source = (Byte*)malloc(sourceLen);
	if (source==NULL)
	{
		return IMREAD_ERR_MEMORY;
	}
	fread( source, 1, sourceLen, theFile );

	uLongf destLen = 0;
	Bytef *dest = Buffer_GetRowAddrAndSize(myBuffer,0,destLen);
	destLen *= myBuffer->totalLines;
	//fprintf(stderr,"destlen: %li\n",destLen);

	int err = uncompress( dest, &destLen, source, sourceLen );

	ImReadError_t errret = IMREAD_ERR_NO;
	switch (err)
	{
		case Z_OK:
			break;
		case Z_MEM_ERROR:
			errret = IMREAD_ERR_MEMORY;
			break;
		case Z_BUF_ERROR:
			{	// try with larger memory block, TL 07.01.10
				uLongf nLargerLen = destLen * 15/10;
				Bytef *pLargerDest = (Bytef*)malloc( nLargerLen );
				if (pLargerDest)
				{
					err = uncompress( pLargerDest, &nLargerLen, source, sourceLen );
					if (err==Z_OK)
					{	// copy needed data
						memcpy( dest, pLargerDest, destLen );
					}
					free(pLargerDest);
				}
			}
			if (err!=Z_OK)
			{	// problem
				//"Output buffer too small for uncompressed data!"
				errret = IMREAD_ERR_MEMORY;
			}
			break;
		case Z_DATA_ERROR:
			// "Compressed data is corrupt!"
			errret = IMREAD_ERR_DATA;
			break;
	}

	free(source);
	return errret;
}



ImReadError_t SCPackFixedBits_Read( FILE* theFile, BufferType* myBuffer, int theValidBits )
{
	if (theValidBits<= 8)
		theValidBits =  8;
	else
//	if (theValidBits<=10)
//		theValidBits = 10;
//	else
	if (theValidBits<=12)
		theValidBits = 12;
//	else
//	if (theValidBits<=14)
//		theValidBits = 14;
	else
		theValidBits = 16;

	Word *dataPtr;
	Word array[16];

	for (int row=0; row<myBuffer->totalLines; row++)
	{
		unsigned long destLen = 0;
		dataPtr = (Word*) Buffer_GetRowAddrAndSize(myBuffer,row,destLen);
		int nx = myBuffer->nx;
		while (nx>0)
		{
			switch (theValidBits)
			{
				case 8:
					fread( array, sizeof(Word), 1, theFile );
					if (nx<2)
					{	// last pixel of a row
						*dataPtr = (array[0] & 0x00FF);
						dataPtr++;
						nx = 0;
					}
					else
					{
						*dataPtr =  (array[0] & 0x00FF);
						dataPtr++;
						*dataPtr = ((array[0] & 0xFF00) >> 8);
						dataPtr++;
						nx -= 2;
					}
					break;
				case 10:
					break;
				case 12:
					if (nx<4)
					{	// last pixel of a row
						fread( dataPtr, sizeof(Word), nx, theFile );
						nx = 0;
					}
					else
					{	// decompress next 4 pixel
						fread( array, sizeof(Word), 3, theFile );
						*dataPtr = (array[0] & 0x0FFF);
						dataPtr++;
						*dataPtr = (array[0] >> 12) | ((array[1] & 0x00FF) << 4);
						dataPtr++;
						*dataPtr = ((array[1] & 0xFF00) >> 8) | ((array[2] & 0x000F) << 8);
						dataPtr++;
						*dataPtr = (array[2] >> 4);
						dataPtr++;
						nx -= 4;
					}
					break;
				case 14:
					break;
				case 16:
					// read complete line in one step
					fread( dataPtr, sizeof(Word), nx, theFile );
					nx = 0;
					break;
			}
		}
	}
	return IMREAD_ERR_NO;
}



void Scale_Read( const char*theData, BufferScaleType* theScale )
{
	int pos;
	sscanf(theData,"%f %f%n",&theScale->factor,&theScale->offset,&pos);
	theScale->unit[0] = 0;
	theScale->description[0] = 0;
	if (pos>0)
	{
		while (theData[pos]==' ' || theData[pos]=='\n')
			pos++;
		strncpy( theScale->unit, theData+pos, sizeof(theScale->unit) );
		theScale->unit[sizeof(theScale->unit)-1] = 0;
		pos++;
		while (theData[pos]!=' ' && theData[pos]!='\n' && theData[pos]!='\0')
			pos++;
		while (theData[pos]==' '|| theData[pos]=='\n')
			pos++;
		strncpy( theScale->description, theData+pos, sizeof(theScale->description) );
		theScale->description[sizeof(theScale->description)-1] = 0;
		// cut unit
		pos = 0;
		while (theScale->unit[pos]!=' ' && theScale->unit[pos]!='\n' && theScale->unit[pos]!='\0')
			pos++;
		theScale->unit[pos] = '\0';
	}
}


int ReadIM7 ( const char* theFileName, BufferType* myBuffer, AttributeList** myList )
{
	FILE* theFile = fopen(theFileName, "rb");				// open for binary read
	if (theFile==NULL)
	   return IMREAD_ERR_FILEOPEN;

	// Read an image in our own IMX or IMG or VEC or VOL format
	int theNX,theNY,theNZ,theNF;
	// read and store file header contents
	Image_Header_7 header;
	if (!fread( (char*)&header, sizeof(header), 1, theFile ))
	{
      fclose(theFile);
      return IMREAD_ERR_HEADER;
   }

	switch (header.version)
	{
		case IMAGE_IMG:
		case IMAGE_IMX:
		case IMAGE_FLOAT:
		case IMAGE_SPARSE_WORD:
		case IMAGE_SPARSE_FLOAT:
		case IMAGE_PACKED_WORD:
			fclose(theFile);
			return ReadIMX(theFileName,myBuffer,myList);
	}

	if (header.isSparse)
	{
      fclose(theFile);
      return IMREAD_ERR_FORMAT;
	}

	theNX = header.sizeX;
	theNY = header.sizeY;
	theNZ = header.sizeZ;
	theNF = header.sizeF;
	bool bFloat = (header.buffer_format > 0 /*vector*/) || (header.buffer_format == BUFFER_FORMAT_FLOAT);
	//fprintf(stderr,"%i %i %i %i\n", theNX,theNY,theNZ,theNF);
	CreateBuffer( myBuffer, theNX,theNY,theNZ,theNF, bFloat, header.vector_grid, (BufferFormat_t)header.buffer_format );

	ImReadError_t errret = IMREAD_ERR_NO;
	//fprintf(stderr,"format=%i pack=%i\n",header.buffer_format,header.pack_type);
	switch (header.pack_type)
	{
		case IM7_PACKTYPE_IMG:
			errret = SCPackUncompressed_Read( theFile, myBuffer, header.buffer_format==BUFFER_FORMAT_MEMPACKWORD );
			break;
		case IM7_PACKTYPE_IMX:
			errret = SCPackOldIMX_Read(theFile,myBuffer);
			break;
		case IM7_PACKTYPE_ZLIB:
			errret = SCPackZlib_Read(theFile,myBuffer);
			break;
		case IM7_PACKTYPE_FIXED_12_0:
			errret = SCPackFixedBits_Read( theFile, myBuffer, 12 );
			break;
		default:
			errret = IMREAD_ERR_FORMAT;
	}
	//fprintf(stderr,"readdata %i\n",errret);

	if (errret==IMREAD_ERR_NO)
	{
		AttributeList* tmpAttrList = NULL;
		AttributeList** useList = (myList!=NULL ? myList : &tmpAttrList);
      ReadImgAttributes(theFile,useList);
		AttributeList* ptr = *useList;
		while (ptr!=NULL)
		{
			//fprintf(stderr,"%s: %s\n",ptr->name,ptr->value);
			if (strncmp(ptr->name,"_SCALE_",7)==0)
			{
				switch (ptr->name[7])
				{
					case 'X':	Scale_Read( ptr->value, &myBuffer->scaleX );	break;
					case 'Y':	Scale_Read( ptr->value, &myBuffer->scaleY );	break;
					case 'I':	Scale_Read( ptr->value, &myBuffer->scaleI );	break;
				}
			}
			ptr = ptr->next;
		}
   }

	fclose(theFile);
	return errret;
}


int WriteIM7 ( const char* theFileName, bool isPackedIMX, BufferType* myBuffer, AttributeList* myList )
{
	int theNX = myBuffer->nx;
	int theNY = myBuffer->ny;
	int theNZ = myBuffer->nz;
	int theNF = myBuffer->nf;
	//fprintf(stderr,"WriteIM7 size %i %i %i %i\n",theNX,theNY,theNZ,theNF);

	FILE* theFile = fopen(theFileName, "wb");				// open for binary write
	if (theFile==NULL)
	   return IMREAD_ERR_FILEOPEN;

	Image_Header_7 header;
	header.version				= 0;
	header.isSparse			= 0;
	header.sizeX				= theNX;
	header.sizeY				= theNY;
	header.sizeZ				= theNZ;
	header.sizeF				= theNF;
	header.scalarN				= 0;
	header.vector_grid	 	= 1;
	header.extraFlags			= 0;
	header.buffer_format 	= (myBuffer->isFloat ? -3 : -4 );	// images float or word
	if (myBuffer->image_sub_type > 0)
	{	// vector
		header.buffer_format = myBuffer->image_sub_type;
		header.vector_grid = myBuffer->vectorGrid;
		theNY *= GetVectorComponents( (BufferFormat_t)header.buffer_format );
	}
	if (myBuffer->isFloat)
	{	// no compression for float and vector
		isPackedIMX = false;
	}
	header.pack_type			= (isPackedIMX ? IM7_PACKTYPE_IMX : IM7_PACKTYPE_IMG);
	if (fwrite( &header, sizeof(header), 1, theFile )!=1)
	{
		fclose(theFile);
		return IMREAD_ERR_HEADER;
	}

	// write data
	if (isPackedIMX)
	{
		int err = WriteIMX( theFile, myBuffer );
		if (err)
		{
			fclose(theFile);
			return IMREAD_ERR_DATA;
		}
	}
	else
	{
		for (int row=0; row<theNY*theNZ*theNF; row++)
		{
			if (myBuffer->isFloat)
				fwrite( &myBuffer->floatArray[row*theNX], sizeof(float), theNX, theFile );
			else
				fwrite( &myBuffer->wordArray[row*theNX], sizeof(Word), theNX, theFile );
		}
	}

	// write attributes
	if (myList)
	{
		WriteImgAttributes( theFile, false, myList );
	}
	else
	{	// just END attribute
		WriteAttribute_END( theFile );
	}

	fclose(theFile);
	return 0;
}
