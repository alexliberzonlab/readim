#!/usr/bin/env python

"""
setup.py file for SWIG example
"""

version = '0.5.1'

#include "Python.h"

from setuptools import setup, find_packages, Extension

import subprocess, sys, os
import glob


try:
    p= subprocess.check_call(['swig', '-python', '-py3', '-c++' ,'-IReadIM/src','ReadIM/core.i'])
except:
    print ('unable to run swig! is it installed?. Will try to perform action anyway...')

scs = ['ReadIMX.cpp', 'ReadIM7.cpp', 'swigExtras.cpp',
        'zlib/adler32.c','zlib/deflate.c','zlib/infcodes.c',
        'zlib/inflate.c','zlib/infutil.c', 'zlib/uncompr.c',
         'zlib/compress.c','zlib/infblock.c','zlib/inffast.c',
        'zlib/inftrees.c','zlib/trees.c','zlib/zutil.c']

scs = ['ReadIM/src/'+s for s in scs]
scs = ['ReadIM/core_wrap.cxx'] + scs
for s in scs:
    assert os.path.isfile(s)

extra_compile_args  =['-IReadIM/src']

ReadIMX_module = Extension('ReadIM._core',
# Auto SWIG doesn't work because the files are outputs 'core.py' to the current directory not ReadIM
##                            ['core.i'], swig_opts=['-c++', '-IReadIM/src'],
# Manual SWIG
                            sources=scs,
                            extra_compile_args = extra_compile_args,
                            )

if len(sys.argv) < 2:
    script_args = ['bdist_wininst']

else:
    script_args = sys.argv[1:]


license_link="""<a rel="license" href="http://creativecommons.org/licenses/by-nc/3.0/">\
<img alt="Creative Commons License" style="border-width:0"\
 src="http://i.creativecommons.org/l/by-nc/3.0/88x31.png" />\
 </a><br />This work is licensed under a <a rel="license"\
  href="http://creativecommons.org/licenses/by-nc/3.0/">Creative Commons\
   Attribution-NonCommercial 3.0 Unported License</a>.
   """
description      = 'Read and write native DaVis images and vectors filetypes VC7 and IM7'
long_description = ''.join(open('README').readlines())


setup (name = 'ReadIM',
        description = description,
       version      = version,
       author       = "Alan Fleming + LaVision",
       author_email =  'alanf@amc.edu.au',
       url          = 'https://bitbucket.org/fleming79/readim',
       license      = 'Creative Commons Attribution-NonCommercial 3.0 Unported License',
       platform     = 'win',
       ext_modules  = [ReadIMX_module],
       packages     = ['ReadIM'],
       package_data = {'ReadIM':['*.dll','sample/*.*']},
       include_package_data = True,
       script_args          = script_args,

       )



