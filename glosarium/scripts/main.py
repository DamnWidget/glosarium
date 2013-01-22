#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
.. module:: glosarium
    :platform: POSIX, Windows
    :synopsis: Command line tool for glosarium

.. moduleauthor:: Oscar Campos <oscar.campos@member.fsf.org>
"""

import os
import sys
from optparse import OptionParser

from glosarium.po_parser import PoParser
from glosarium import __version__ as version
from glosarium.glosary_parser import WebParser, WebParserError


def main():
    """Main application entry point
    """

    opt_parser = OptionParser(usage=(
        'usage: %prog po_file <log_file>\nType %prog -h or --help to get help'
    ))
    opt_parser.add_option(
        '-v', '--version', action='store_true', dest='version',
        help='show program\'s version number and exit'
    )
    opt_parser.add_option(
        '-l', '--lines', action='store_true', dest='lines',
        help='also print lines when a term is found'
    )
    opt_parser.add_option(
        '-r', '--resume', action='store_true', dest='resume',
        help='print a resume when done'
    )
    (options, args) = opt_parser.parse_args()

    if options.version:
        sys.stdout.write('glosarium {0}\n'.format(version))
        sys.exit(0)

    if not len(args):
        opt_parser.error('You must provide the Po file that you want to check')

    if len(args) > 1:
        dest = os.path.abspath(args[1])
    else:
        dest = None

    source = os.path.abspath(args[0])
    try:
        glosary = WebParser().glosary
    except WebParserError, error:
        print error
        sys.exit(1)

    result, resume = PoParser(
        glosary, source, options.resume, options.lines).parse()
    buffer = '\n'.join(result)

    if options.resume:

        buffer += '\n\n+{0}+\n'.format('-' * 77)
        buffer += '| Term {0:24} | Appears in lines {1:26} |\n'.format(
            ' ', ' ')
        buffer += '+{0}+\n'.format('-' * 77)
        for k, v in resume.iteritems():
            buffer += '| {term:30}| {data:43} |\n'.format(
                term=k[:30], data=str(v), num=len(v)
            )
        buffer += '+{0}+\n'.format('-' * 77)
        buffer += '| Total {num} terms {void:60} |\n'.format(
            num=len(resume), void=''
        )
        buffer += '+{0}+\n'.format('-' * 77)

    print '\n{0}'.format(buffer)
    if dest is not None:
        with open(dest, 'w') as fd:
            fd.write(buffer)

            print '\n\nFile {file} has been written to the drive\n'.format(
                file=dest
            )

if __name__ == '__main__':
    main()
