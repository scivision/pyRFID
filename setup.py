#!/usr/bin/env python
from setuptools import setup #enables develop

req = ['nose','pygame','pandas','scipy','pyserial']

setup(name='pyRFID',
      packages=['pyrfid'],
	  description='Example of reading RFID tag and playing sound with XLSX read',
	  author='Michael Hirsch, Ph.D.',
	  url='https://github.com/scienceopen/pyRFID',
	  classifiers=[
	        'Programming Language :: Python :: 3.6',
	        ],
	  install_requires=req,
	  )
