#!/usr/bin/env python

"""
setup.py file for SWIG example
"""

version = '0.5.0'

#include "Python.h"
from distribute_setup import use_setuptools
use_setuptools()

##from distutils.core import setup, Extension

from setuptools import setup, find_packages, Extension

import subprocess, sys, os
import glob


try:
    p= subprocess.check_call(['swig', '-python', '-c++' ,'-IReadIM/src','ReadIM/core.i'])
except:
    print 'unable to run swig! is it installed?. Will try to perform action anyway...'

scs = ['ReadIMX.cpp', 'ReadIM7.cpp', 'swigExtras.cpp',
        'zlib/adler32.c','zlib/deflate.c','zlib/infcodes.c',
        'zlib/inflate.c','zlib/infutil.c', 'zlib/uncompr.c',
         'zlib/compress.c','zlib/infblock.c','zlib/inffast.c',
        'zlib/inftrees.c','zlib/trees.c','zlib/zutil.c']

scs = ['ReadIM/src/'+s for s in scs]
scs = ['ReadIM/core_wrap.cxx'] + scs
for s in scs:
    assert os.path.isfile(s)

extra_link_args     = []#['-IReadIM/src', '-IReadIM/src/zlib']
extra_compile_args  =['-IReadIM/src', '-IReadIM/src/zlib']
##ifile               = os.path.abspath('ReadIM/core.i')
##assert os.path.isfile(ifile)

ReadIMX_module = Extension('ReadIM._core',
##                            ['ReadIM/core.i'],
##                            swig_opts=['-modern', '-c++', '-IReadIM/src'],
                            sources=scs,
                            extra_compile_args = extra_compile_args,
                            extra_link_args = extra_link_args)
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

sys.path.insert(1, os.path.abspath('ReadIM')) # to give access to core.py

setup (name = 'ReadIM_bin',
       version = version,
       author      = "Alan Fleming + LaVision",
       description = "Python wrapper for reading and writing LaVision IMX files. Thanks to LaVision for providing original code.",
       ext_modules = [ReadIMX_module],
       py_modules = ['configobj'],
       packages = ['ReadIM'],
       package_data = {'ReadIM':['*.dll','sample/*.*']},
       include_package_data = True,
       install_requires=['setuptools'],
       script_args = script_args,
       license = license
       )



