# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os
import sys

setup(
    name = "textclassifier",
    version = "1.2",
    packages = find_packages(),
    package_data = {
        'textclassifier.texts': ['*.txt', '*.def', '*.csv', '*.xlsx']
    },

    author       = "University of Tartu",
    author_email = "tpetmanson@gmail.com",
    description  = "Machine learning software for organizing data into categories",
    license      = "GPLv2",
    url          = "https://github.com/estnltk/textclassifier",


    # we have fixed dependency versions to guarantee, what works
    # however, you can probably safely install newer versions of the dependencies
    install_requires = [
        'estnltk==1.2'                     # estnltk dependency
        ],

    classifiers = ['Intended Audience :: Developers',
                   'Intended Audience :: Education',
                   'Intended Audience :: Science/Research',
                   'Intended Audience :: Information Technology',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.4',
                   'Topic :: Scientific/Engineering',
                   'Topic :: Scientific/Engineering :: Artificial Intelligence',
                   'Topic :: Scientific/Engineering :: Information Analysis',
                   'Topic :: Text Processing',
                   'Topic :: Text Processing :: Linguistic']
)
