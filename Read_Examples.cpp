/* Read_Examples: Examples for usage of the ReadDLL functions
	(c) LaVision 2001-2011, TL

	The Read_GeneralExample code gives an example for the general usage of
	the ReadIMX and ReadIM7 functions. The code loads a IMG/IMX/VEC file or a IM7/VC7,
	prints out the size and type of the image or vector file and stores the raw data in a TXT file.
	When the files are compiled on a Linux system, the executable can be called
	with the filename as parameter and then call Read_GeneralExample.

	The Write_GeneralExample code gives an example for writing IM7 files.

	The ReadIMX_cl function can be called with the CL code above of the function code.
	This function loads a IMG/IMX/IM7/VEC/VC7 file into a DaVis buffer.

  	The WriteIMG_cl function can be called with the CL code above of the function code.
	This function stores a DaVis buffer as IMG file.
*/

#include "ReadIMX.h"
#include "ReadIM7.h"


/*****************************************************************************/
/* General Example                                                           */
/*****************************************************************************/

// Return TRUE if theBuffer is of vector type.
bool BufferType_GetVectorSize( const BufferType& theBuffer, int& theWidth, int& theHeight )
{
	if (theBuffer.image_sub_type<=0)
	{	// image
		return false;
	}
	const int compN[] = { 1, 9, 2, 10, 3, 14 };
	theHeight = theBuffer.ny / compN[theBuffer.image_sub_type];
	theWidth  = theBuffer.nx;
	return true;
}


// Return TRUE if the vector exists
bool BufferType_GetVector( const BufferType& theBuffer, int theX, int theY, int theFrame, float& vx, float& vy, float& vz )
{
	vx=vy=vz = 0;

	int frameOffset = theFrame * theBuffer.nx * theBuffer.ny * theBuffer.nz;
	int width, height;
	BufferType_GetVectorSize( theBuffer, width, height );
	int componentOffset = width * height;
	int mode;

	if (theX<0 || theX>=width || theY<0 || theY>=height || theFrame<0 || theFrame>=theBuffer.nf)
	{	// invalid position
		return false;
	}

	switch (theBuffer.image_sub_type)
	{
		case 0:	// it's an image and no vector buffer
			return false;
		case 1:	//	PIV vector field with header and 4*2D field
			mode = (int) theBuffer.floatArray[ theX + theY*width + frameOffset ];
			if (mode<=0)	// disabled vector
				return true;
			if (mode>4)		// interpolated or filled vector
				mode = 1;
			mode--;
			vx = theBuffer.floatArray[ theX + theY*width + frameOffset + componentOffset*(mode*2+1) ];
			vy = theBuffer.floatArray[ theX + theY*width + frameOffset + componentOffset*(mode*2+2) ];
			break;
		case 2:	//	simple 2D vector field
			vx = theBuffer.floatArray[ theX + theY*width + frameOffset ];
			vy = theBuffer.floatArray[ theX + theY*width + frameOffset + componentOffset ];
			break;
		case 3:	// same as 1 + peak ratio
			mode = (int) theBuffer.floatArray[ theX + theY*width + frameOffset ];
			if (mode<=0)	// disabled vector
				return true;
			if (mode>4)		// interpolated or filled vector
				mode = 1;
			mode--;
			vx = theBuffer.floatArray[ theX + theY*width + frameOffset + componentOffset*(mode*2+1) ];
			vy = theBuffer.floatArray[ theX + theY*width + frameOffset + componentOffset*(mode*2+2) ];
			break;
		case 4:	// simple 3D vector field
			vx = theBuffer.floatArray[ theX + theY*width + frameOffset ];
			vy = theBuffer.floatArray[ theX + theY*width + frameOffset + componentOffset ];
			vz = theBuffer.floatArray[ theX + theY*width + frameOffset + componentOffset*2 ];
			break;
		case 5:	//	PIV vector field with header and 4*3D field + peak ratio
			mode = (int) theBuffer.floatArray[ theX + theY*width + frameOffset ];
			if (mode<=0)	// disabled vector
				return true;
			if (mode>4)		// interpolated or filled vector
				mode = 1;
			mode--;
			vx = theBuffer.floatArray[ theX + theY*width + frameOffset + componentOffset*(mode*3+1) ];
			vy = theBuffer.floatArray[ theX + theY*width + frameOffset + componentOffset*(mode*3+2) ];
			vz = theBuffer.floatArray[ theX + theY*width + frameOffset + componentOffset*(mode*3+3) ];
			break;
	}
	return true;
}


int Read_GeneralExample( const char* p_sFileName, const char* p_sResultName, bool p_bHeader, bool p_bAttributes )
{
	BufferType myBuffer;
	fprintf(stderr,"Reading '%s'...\n",p_sFileName);

	AttributeList *pAttrList = NULL;
	int err = ReadIM7( p_sFileName, &myBuffer, (p_bAttributes ? &pAttrList : NULL) );
	if (err!=0)
	{
		switch (err)
		{
			case IMREAD_ERR_FILEOPEN:
				fprintf(stderr,"Input file '%s' not found!\n",p_sFileName);
				break;
			case IMREAD_ERR_HEADER:
				fprintf(stderr,"Error in header\n");
				break;
			case IMREAD_ERR_FORMAT:
				fprintf(stderr,"Packing format not supported\n");
				break;
			case IMREAD_ERR_DATA:
				fprintf(stderr,"Error while reading data\n");
				break;
			case IMREAD_ERR_MEMORY:
				fprintf(stderr,"Error out of memory\n");
				break;
			default:
				fprintf(stderr,"Unknown error %i\n",err);
		}
		return 1;
	}

	fprintf(stderr,"File-Info: '%s'\n",p_sFileName);
	fprintf(stderr," Size: %i x %i x %i x %i\n", myBuffer.nx, myBuffer.ny, myBuffer.nz, myBuffer.nf );
	fprintf(stderr," X-Scale: %f * x + %f %s (%s)\n", myBuffer.scaleX.factor, myBuffer.scaleX.offset, myBuffer.scaleX.unit, myBuffer.scaleX.description );
	fprintf(stderr," Y-Scale: %f * x + %f %s (%s)\n", myBuffer.scaleY.factor, myBuffer.scaleY.offset, myBuffer.scaleY.unit, myBuffer.scaleY.description );
	fprintf(stderr," I-Scale: %f * x + %f %s (%s)\n", myBuffer.scaleI.factor, myBuffer.scaleI.offset, myBuffer.scaleI.unit, myBuffer.scaleI.description );
	switch (myBuffer.image_sub_type)
	{
		case BUFFER_FORMAT_IMAGE:
			fprintf(stderr," Type: Image\n");
			break;
		case BUFFER_FORMAT_MEMPACKWORD:
			fprintf(stderr," Type: byte Image\n");
			break;
		case BUFFER_FORMAT_FLOAT:
			fprintf(stderr," Type: float Image\n");
			break;
		case BUFFER_FORMAT_WORD:
			fprintf(stderr," Type: word Image\n");
			break;
		case BUFFER_FORMAT_DOUBLE:
			fprintf(stderr," Type: double Image\n");
			break;
		default:
		{
			const char *TypeName[] = { "Image", "2D-PIV-Vector (header, 4x(Vx,Vy))", "2D-Vector (Vx,Vy)",
												"2D-PIV+p.ratio (header, 4x(Vx,Vy), peakratio)",
												"3D-Vector (Vx,Vy,Vz)", "3D-Vector+p.ratio (header, 4x(Vx,Vy), peakratio)" };
			fprintf(stderr," Type: %s\n", TypeName[myBuffer.image_sub_type]);
			fprintf(stderr," Gridsize: %i\n", myBuffer.vectorGrid);
		}
	}

	fprintf(stderr,"Writing '%s'...\n",p_sResultName);
	FILE* fout = fopen(p_sResultName,"w");
	if (fout==NULL)
	{
		fprintf(stderr,"Can't create output file!\n");
		DestroyBuffer(&myBuffer);
		if (pAttrList)
			DestroyAttributeList( &pAttrList );
		return 1;
	}

	if (p_bHeader)
	{	// print header line with size of image: <points per line> <width> <height> <frames>
		fprintf(fout,"%i %i %i %i\n", myBuffer.nx, myBuffer.nx, myBuffer.ny, myBuffer.nf );
	}
	if (p_bAttributes)
	{	// print all attributes: <name> = <value>
		AttributeList *pAttr = pAttrList;
		while (pAttr)
		{
			char *ptr;
			while ((ptr = strchr(pAttr->value,'\n')) != 0)
				*ptr = '\t';
			fprintf(fout,"%s = %s\n", pAttr->name, pAttr->value );
			pAttr = pAttr->next;
		}
	}

	int x,y,iFrame;
	for (iFrame=0; iFrame<myBuffer.nf; iFrame++)
	{
		for (y=0; y<myBuffer.ny; y++)
		{
			if (myBuffer.isFloat)
				for (x=0; x<myBuffer.nx; x++)
					fprintf(fout,"%10.3f ", myBuffer.floatArray[iFrame*myBuffer.nx*myBuffer.ny+y*myBuffer.nx+x] );
			else
				for (x=0; x<myBuffer.nx; x++)
					fprintf(fout,"%i\t", myBuffer.wordArray[iFrame*myBuffer.nx*myBuffer.ny+y*myBuffer.nx+x] );
			fprintf(fout,"\n");
		}
	}
	fclose(fout);

	// now we have to delete the buffer data
	DestroyBuffer(&myBuffer);
	if (pAttrList)
		DestroyAttributeList( &pAttrList );

	return 0;
}


int Write_GeneralExample( const char* p_sFileName )
{
	BufferType myBuffer;
	fprintf(stderr,"Creating float image buffer\n");
	int sizeX = 10;
	int sizeY = 20;
	int sizeF = 1;
	CreateBuffer( &myBuffer, sizeX, sizeY, 1, sizeF, true, 1, BUFFER_FORMAT_IMAGE );

	int x,y,fr;
	for (fr=0; fr<sizeF; fr++)
	{
		for (y=0; y<sizeY; y++)
		{
			for (x=0; x<sizeX; x++)
			{
				myBuffer.floatArray[fr*sizeY*sizeX+y*sizeX+x] = (float)(y*x) * (fr==0?1:-1);
			}
		}
	}

	// create some test attributes
	AttributeList *myAttributes = NULL;
	SetAttribute( &myAttributes, "TestAttribute1", "Value1" );
	SetAttribute( &myAttributes, "TestAttribute2", "Value2" );

	fprintf(stderr,"Writing '%s'...\n",p_sFileName);
	int err = WriteIM7( p_sFileName, true, &myBuffer, myAttributes );

	// now we have to delete the buffer data
	DestroyBuffer(&myBuffer);
	if (myAttributes)
		DestroyAttributeList( &myAttributes );

	return err;
}


int Write_VectorExample( const char* p_sFileName )
{
	BufferType myBuffer;
	fprintf(stderr,"Creating vector buffer\n");
	int sizeX = 10;
	int sizeY = 10;
	int sizeF = 2;
    sizeY *= 2;	// two components
	CreateBuffer( &myBuffer, sizeX, sizeY, 1, sizeF, true, 32/*grid*/, BUFFER_FORMAT_VECTOR_2D );


	int x,y,fr;
	for (fr=0; fr<sizeF; fr++)
	{
		for (y=0; y<sizeY; y++)
		{
			for (x=0; x<sizeX; x++)
			{
				myBuffer.floatArray[fr*sizeY*sizeX+y*sizeX+x] = (float)(y*x) * (fr==0?1:-1);
			}
		}
	}

	// create some test attributes
	AttributeList *myAttributes = NULL;
	SetAttribute( &myAttributes, "TestAttribute1", "Value1" );
	SetAttribute( &myAttributes, "TestAttribute2", "Value2" );

	fprintf(stderr,"Writing '%s'...\n",p_sFileName);
	int err = WriteIM7( p_sFileName, true, &myBuffer, myAttributes );

	// now we have to delete the buffer data
	DestroyBuffer(&myBuffer);
	if (myAttributes)
		DestroyAttributeList( &myAttributes );

	return err;
}
