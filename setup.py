#!/usr/bin/env python

# Copyright (c) 2013 Oscar Campos <oscar.campos@member.fsf.org>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Distutils installer for Glosarium.
"""

import sys
if not hasattr(sys, "version_info") or sys.version_info < (2, 6):
    raise RuntimeError("Glosarium requires Python 2.6 or later.")

from setuptools import setup, find_packages

from glosarium import __version__ as version

long_description = '''
This is a cross-platform application used by the Spanish Transalation Team of
the GNU Project. It was written by Oscar Campos oscar.campos@member.fsf.org
and released under the GNU General Public License, version 3 or later.
'''

setup(
    name='Glosarium',
    version=version,
    description=('Glosarium parser'),
    long_description=long_description,
    author='Oscar Campos',
    author_email='oscar.campos@member.fsf.org',
    url='http://www.gnu.org/server/standards/transaltions/es/index.html',
    license='GPL',
    packages=find_packages(),
    test_suite='tests',
    install_requires=['httplib2>=0.6'],
    requires=['httplib2(>=0.6)'],
    entry_points={
        'console_scripts': [
            'glosarium = glosarium.scripts.main:main',
        ]
    },
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 2.6',
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',
        'Topic :: Text Processing :: Linguistic'
    ],
)
