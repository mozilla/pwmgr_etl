#!/usr/bin/env python

from setuptools import setup, find_packages
from distutils.core import setup

setup(name='pwmgr_dataset',
      version='0.1',
      description='ETL job to process password manager histograms',
      author='Leif Oines',
      author_email='loines@mozilla.com',
      url='https://github.com/mozilla/pwmgr_etl',
      packages=find_packages(exclude=['tests']),
)
