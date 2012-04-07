#ifndef __READ_EXAMPLES_H
#define __READ_EXAMPLES_H

#include "ReadIMX.h"
#include "ReadIM7.h"

bool BufferType_GetVectorSize( const BufferType& theBuffer, int& theWidth, int& theHeight );
bool BufferType_GetVector( const BufferType& theBuffer, int theX, int theY, int theFrame, float& vx, float& vy, float& vz );
int Write_GeneralExample( const char* p_sFileName );
int Write_VectorExample( const char* p_sFileName );
#endif
