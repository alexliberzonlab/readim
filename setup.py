#!/usr/bin/env python

"""
setup.py file for SWIG example
"""
#include "Python.h"
from distutils.core import setup, Extension
import subprocess, sys

try:
    p= subprocess.check_call(['swig', '-python', '-c++' ,'ReadIM.i'])
except:
    print 'unable to run swig! is it installed?. Will try to perform action anyway...'

scs = ['ReadIM_wrap.cxx', 'ReadIMX.cpp', 'ReadIM7.cpp', 'swigExtras.cpp',
        r'zlib\adler32.c',r'zlib\deflate.c',r'zlib\infcodes.c',
        r'zlib\inflate.c',r'zlib\infutil.c', r'zlib\uncompr.c',
         r'zlib\compress.c',r'zlib\infblock.c',r'zlib\inffast.c',
        r'zlib\inftrees.c',r'zlib\trees.c',r'zlib\zutil.c']

ReadIMX_module = Extension('_ReadIM',
                           sources=scs,
                           )
if len(sys.argv) < 2:
    script_args = ['build', '--compiler=mingw32', 'install', 'bdist_wininst']
##    script_args = ['build', '--plat-name=win32','--compile=mingw32', 'bdist_wininst'] # does not really work for a 32 bit system
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
       version = '0.2',
       author      = "Alan Fleming + LaVision",
       description = "Python wrapper for reading and writing LaVision IMX files. Thanks to LaVision for providing original code.",
       ext_modules = [ReadIMX_module],
       py_modules = ["ReadIM", "ReadIMextra"],
       script_args = script_args,
       license = license
       )



