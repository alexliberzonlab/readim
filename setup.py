#!/usr/bin/env python

"""
setup.py file for SWIG example
"""
#include "Python.h"
from distutils.core import setup, Extension
import zlib, subprocess, sys

p= subprocess.check_call(['swig', '-python', '-c++' ,'ReadIM.i'])

scs = ['ReadIM_wrap.cxx', 'ReadIMX.cpp', 'ReadIM7.cpp', 'swigExtras.cpp',
        r'zlib\adler32.c',r'zlib\deflate.c',r'zlib\infcodes.c',
        r'zlib\inflate.c',r'zlib\infutil.c', r'zlib\uncompr.c',
         r'zlib\compress.c',r'zlib\infblock.c',r'zlib\inffast.c',
        r'zlib\inftrees.c',r'zlib\trees.c',r'zlib\zutil.c']

ReadIMX_module = Extension('_ReadIM',
                           sources=scs,
                           )
if len(sys.argv) < 2:
    script_args = ['bdist_wininst']
else:
    script_args = sys.argv[1:]

license = """This is the license\n"""
license_link="""<a rel="license" href="http://creativecommons.org/licenses/by-nc/3.0/">\
<img alt="Creative Commons License" style="border-width:0"\
 src="http://i.creativecommons.org/l/by-nc/3.0/88x31.png" />\
 </a><br />This work is licensed under a <a rel="license"\
  href="http://creativecommons.org/licenses/by-nc/3.0/">Creative Commons\
   Attribution-NonCommercial 3.0 Unported License</a>.
   """
setup (name = 'ReadIM',
       version = '0.1',
       author      = "Alan Fleming + DaVis",
       description = "Python wrapper for reading and writing LaVision IMX files",
       ext_modules = [ReadIMX_module],
       py_modules = ["ReadIM"],
       script_args = script_args,
       license = license
       )


