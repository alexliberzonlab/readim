/* File: ReadIM.i */
%module ReadExamples
 %include "cpointer.i"
 %include "carrays.i"

//%{
// #define SWIG_FILE_WITH_INIT
// %}

%{
 /* Includes the header in the wrapper code */
// #include "ReadIMX.h"
 #include "Read_Examples.h"
// #include "ReadIM7.h"
 #include "python.h"
// #include "swigExtras.h"
 %}

 /* Parse the header file to generate wrappers */
 %include "Read_Examples.h"
// %array_class(unsigned short, useintArray);
// %array_class(float, usefloatArray);


/* Create some functions for working with "int *" */
 %pointer_functions(int,intp);
 %pointer_functions(float, floatp);

/* A function that uses an "int *" */
//void add(int x, int y, int *result);

