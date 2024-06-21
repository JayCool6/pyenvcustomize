#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：setup.py
# @Author  ：Jay
# @Date    ：2024/6/21 18:41 
# @Remark  ：
from setuptools import setup, find_packages
import io

with io.open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyenvcustomize',
    version='1.0.0',
    description='Automatically create or update sitecustomize.py in the Python environment',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Jay',
    url='https://github.com/jaygarage/pyenvcustomize',
    packages=find_packages(),
    install_requires=[],  # 如果有依赖库可以在这里添加
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
