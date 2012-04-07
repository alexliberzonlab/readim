#!/usr/bin/env python

"""
setup_ex.py
"""
#include "Python.h"
from distutils.core import setup, Extension
import zlib, subprocess

p= subprocess.check_call(['swig', '-python', '-c++' ,'ReadExamples.i'])

scs = ['ReadExamples_wrap.cxx','Read_Examples.cpp', 'ReadIMX.cpp', 'ReadIM7.cpp', 'swigExtras.cpp',
        r'zlib\adler32.c',r'zlib\deflate.c',r'zlib\infcodes.c',
        r'zlib\inflate.c',r'zlib\infutil.c', r'zlib\uncompr.c',
         r'zlib\compress.c',r'zlib\infblock.c',r'zlib\inffast.c',
        r'zlib\inftrees.c',r'zlib\trees.c',r'zlib\zutil.c']

_module = Extension('_ReadExamples', sources = scs)
script_args = ['install']
setup (name = 'ReadExamples',
       version = '0.1',
       author      = "LaVision - wrapped by Alan Fleming",
       description = "Python wrapper for reading and writing LaVision IMX files",
       ext_modules = [_module],
       py_modules = ["ReadExamples"],
       script_args = script_args
       )
