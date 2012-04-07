/* File: ReadIM.i */
%module ReadIM
%include "cpointer.i"
%include "carrays.i"

%{
 #define SWIG_FILE_WITH_INIT
 %}

%{
 /* Includes the header in the wrapper code */
 #include "ReadIMX.h"
 #include "ReadIM7.h"
 #include "python.h"
 #include "swigExtras.h"
 %}

 /* Parse the header file to generate wrappers */
 %include "ReadIMX.h"
 %include "ReadIM7.h"
 %include "swigExtras.h"
 %pointer_functions(int,intp);
 %pointer_functions(float, floatp);
 %pointer_class(double, dPtr);
 %pointer_class(char, cPtr);
 %array_class(unsigned short, useintArray);
 %array_class(float, usefloatArray);
 %array_class(double, usedoubleArray);
 /* AttributeList ** alan3 (AttributeList * al); */
 /*int getname (AttributeList ** ptr, char * str); */

/*extern void add(double a, double b, double * result);*/
