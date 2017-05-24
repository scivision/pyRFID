#!/usr/bin/env python
req = ['nose','pandas','scipy','pyserial']
pipreq = ['pygame',]
import pip
try:
    import conda.cli
    conda.cli.main('install',*req)
except Exception as e:    
    pip.main(['install'] + req)
pip.main(['install'] + pipreq)
   
# %%
from setuptools import setup #enables develop

setup(name='pyRFID',
      packages=['pyrfid'],
	  description='Example of reading RFID tag and playing sound with XLSX read',
	  author='Michael Hirsch, Ph.D.',
	  url='https://github.com/scivision/pyRFID',
	  classifiers=[
	        'Programming Language :: Python :: 3.6',
	        ],
	  )
