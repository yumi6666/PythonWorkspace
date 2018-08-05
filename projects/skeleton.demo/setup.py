# -*- coding:utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutil.core import setup
    
config={
    'description': 'My Project',
    'author': '',
    'url':'',
    'download_url':'',
    'author_email':'',
    'version':'',
    'install_requires':['nose'],
    'packages':['NAME'],
    'scripts':[],
    'name': 'proj_name'
}

setup(**config)