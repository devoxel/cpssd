#!/usr/bin/env python

from distutils.core import setup

setup( name='thunk',
       version='0.1.0',
       description='Text Based Adventure Game',
       author='Aaron Delaney',
       author_email='aaron.delaney29@mail.dcu.ie',
       packages=['thunk', 'thunk.engine', 'thunk.assets'],
       scripts=['run/thunk.py'],
       install_requires=[
          'pytest',
      ],
)
