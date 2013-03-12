# -*- encoding: utf-8 -*-

from distutils.core import setup

# reflect changes in "CHANGES.rst"
version = '0.1'

# package description
desc = "Knecht is a micro Content Management System (CMS) for static blog generators"

long_desc = []
for _file in ('README.md', 'CHANGES.rst'):
    with open(_file, 'r') as fh:
        long_desc.append(fh.read())

setup(
    name='knecht',
    version=version,
    description=desc,
    long_description='\n\n'.join(long_desc),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "License :: BSD 2 clauses",
        "Operating System :: Unix",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    ], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Christoph Polcin <labs@polcin.de>, Frank Schneider <shoul@gmx.de>',
    author_email='dev@polcin.de',
    license='BSD',
    py_modules=['knecht.__init__'],
)
