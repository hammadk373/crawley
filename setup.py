#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

PATH = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join("crawley", "conf", "templates")
templates_local_dir = os.path.join(PATH, templates_dir)
templates_files = [os.path.join(templates_dir, file) for file in os.listdir(templates_local_dir)]

setup(
    name="crawley",
    version="0.1.0",
    description="Pythonic Scraping / Crawling FrameWork built On Eventlet",
    author="Crawley Developers",
    author_email = "jmg.utn@gmail.com",
    license = "GPL v3",
    keywords = "Scraping Crawling Framework Python",
    packages=find_packages(exclude=["tests"]),      
    data_files=[
        (templates_dir, templates_files)
    ],
    include_package_data=True,    
    scripts=['crawley/bin/crawley'],    
    install_requires=[
        'lxml',
        'eventlet',
        'elixir',
        'pyquery',        
    ],
    url='http://crawley-project.com.ar/',
)
