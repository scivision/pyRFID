#!/usr/bin/env python
install_requires = ['pandas','scipy','pyserial','pygame',]
tests_require=['nose','coveralls']
# %%
from setuptools import setup,find_packages

setup(name='pyRFID',
      packages=find_packages(),
	  description='Example of reading RFID tag and playing sound with XLSX read',
	  author='Michael Hirsch, Ph.D.',
	  url='https://github.com/scivision/pyRFID',
	  classifiers=[
	        'Programming Language :: Python :: 3',
	        ],
      python_requires='>=3.6',
      install_requires=install_requires,
      tests_require=tests_require,
      extras_require={'tests':tests_require},
	  )
