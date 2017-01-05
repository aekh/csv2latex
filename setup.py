"""
A small program for efficiently and painlessly convert csv-files to LaTeX-tables of variable sizes.
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='csv2latex',
    version='0.1.0',
    description='A small program for efficiently and painlessly convert csv-files to LaTeX-tables of variable sizes.',
    long_description=long_description,
    url='https://github.com/aekh/csv2latex',
    author='Alexander Ek (aekh)',
    author_email='ekh.alex@gmail.com',
    license='GPLv3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GPLv3',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    entry_points={
        'console_scripts': [
            'csv2latex=csv2latex:main',
        ],
    },
)