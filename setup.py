#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import codecs
import os

from setuptools import (
    find_packages,
    setup,
)


def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='funcat',
    version=read('funcat/VERSION.txt'),
    description='funcat',
    packages=find_packages(exclude=[]),
    author='Hua Liang',
    url='https://github.com/cedricporter/funcat',
    author_email='et@everet.org',
    license='Apache License v2',
    package_data={'': ['*.*']},
    install_requires=read("requirements.txt"),
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
