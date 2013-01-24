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
.. module:: po_parser
    :platform: POSIX, Windows
    :synopsis: This module locates in a text file the given glosary terms

.. moduleauthor:: Oscar Campos <oscar.campos@member.fsf.org>
"""

import re


class PoParserError(Exception):
    """Class for PoParser exceptions
    """


class PoParser(object):
    """
    I parse a file looking for a given tuple of terms

    :param terms: the terms to find
    :type terms: tuple
    :param file: the file where to find
    :type file: str
    """

    def __init__(self, glosary, pofile, resume=False, online=False):
        self.glosary = glosary
        self.pofile = pofile
        self.resume = resume
        self.online = online
        self.skip = re.compile(
            r'(href=\\?"\\?\b(https?|ftp|file'
            '|mailto):/?/?\S+"|src=\\?"\b\S+"|^#.*)'
        )
        self.match = r'(\b{0}\b)'

    def parse(self):
        """I parse the po file looking for glosary terms
        """

        lines = self._load_file()

        result = []
        resume = {}

        for i in range(len(lines)):
            for term in self.glosary.keys():
                if re.search(self.match.format(term), lines[i], re.IGNORECASE):
                    # skip matches on href urls or src properties
                    match = self.skip.search(lines[i])
                    if match is not None:
                        if term.lower() in match.group().lower():
                            continue

                    if self.resume and term not in resume:
                        resume[term] = []
                        resume[term].append(i + 1)

                    result.append(
                        'Term {term} found in line {line}\n  possible '
                        'translations: {trans}\n'.format(
                            term=term, line=i + 1, trans=self.glosary[term]
                        )
                    )
                    if self.online:
                        result.append('|__\n    ' + lines[i])

        return result, resume

    def _load_file(self):
        """I load the file from the file system
        """

        regex = re.compile(r'#. TRANSLATORS: Use space \(SPC\)')
        lines = []
        with open(self.pofile, 'r') as file_descriptor:
            while True:
                line = file_descriptor.readline()
                if regex.search(line) is not None:
                    break
                lines.append(line)

        return lines
