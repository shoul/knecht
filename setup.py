# -*- encoding: utf-8 -*-

from os.path import join, dirname
from setuptools import setup, find_packages

# reflect changes in "CHANGES.rst"
version = '0.1'

# package description
desc = "Knecht is a micro Content Management System (CMS) for static blog compiler"

requires = ['Flask>=0.9']

setup(
    name='knecht',
    version=version,
    author='Christoph Polcin <labs@polcin.de>, Frank Schneider <shoul@gmx.de>',
    author_email='dev@polcin.de',
    license='BSD',
    url='https://git.christoph-polcin.com/knecht/',
    description=desc,
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Topic :: Internet",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: News/Diary",
       "Development Status :: 4 - Beta",
        "Environment :: Console",
        "License :: BSD 2 clauses",
        "Operating System :: Unix",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    ], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    install_requires=requires,
    keywords='',
    py_modules=['knecht.__init__'],
)
