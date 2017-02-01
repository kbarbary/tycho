#!/usr/bin/env python

import os
import re
import sys

from setuptools import setup
from setuptools.extension import Extension
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    """Enables setup.py test"""

    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def run_tests(self):
        #import here, because outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

# Synchronize version from code.
fname = os.path.join("tycho", "version.py")
version = re.findall(r"__version__ = \"(.*?)\"", open(fname).read())[0]

classifiers = [
    "Development Status :: 3 - Alpha",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Topic :: Scientific/Engineering :: Astronomy",
    "Intended Audience :: Science/Research"]

setup(name="tycho", 
      version=version,
      description="Photometric supernova light curve typer",
      long_description="",
      license="MIT",
      classifiers=classifiers,
      url="http://github.com/kbarbary/tycho",
      author="Kyle Barbary",
      author_email="kylebarbary@gmail.com",
      #ext_modules=extensions,
      packages=["tycho"],
      scripts=["scripts/tycho"],
      #install_requires=["numpy>=1.5.0",
      #                  "scipy>=0.9.0",
      #                  "astropy>=1.0.0",
      #                  "extinction>=0.3.0",
      #                  "sncosmo>=1.4.0"],
      cmdclass={'test': PyTest})
