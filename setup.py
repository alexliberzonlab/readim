#!/usr/bin/env python

"""
setup.py file readim

run python setup.py [operation]

operations
----------
swig    : Rerun swig. Not required unless changes to code.
build | install | bdist_wininst etc: typical build commands.
test: run the test suite.


"""

version = '0.6.1'

#include "Python.h"

from setuptools import setup, Extension

import subprocess, sys, os
import glob


script_args = sys.argv[1:]

if script_args[0] == 'test':

    # works only when called from this folder
    pth = sys.path.pop(0)
    pth_tests = os.path.join(pth, 'ReadIM')
    print('test path:', pth_tests)
    assert os.path.isdir(pth_tests)
    sys.path.insert(0, pth_tests)
    from tests.test_ReadIM import *
    run_module_suite()
    # restore path
    sys.path.pop(0)
    sys.path.insert(0, pth)

elif script_args[0] == 'test':
    try:
        args = ['swig', '-python','-c++' ,'-IReadIM/src','ReadIM/core.i']
        p= subprocess.check_call(args)
    except:
        print ('unable to run swig! is it installed?. Will try to perform action anyway...')

else:


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

    description      = 'Read and write native DaVis images and vectors filetypes VC7 and IM7'
    long_description = ''.join(open('README').readlines())


    setup (name = 'ReadIM',
            description = description,
           version      = version,
           author       = "Alan Fleming + LaVision",
           author_email =  'alanf@amc.edu.au',
           url          = 'https://bitbucket.org/fleming79/readim',
           ext_modules  = [ReadIMX_module],
           packages     = ['ReadIM'],
           package_data = {'ReadIM':['sample_files/*.*']},
           include_package_data = True,
           script_args          = script_args,

           )



