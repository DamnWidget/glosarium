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
.. module:: test_po_parser
    :platform: POSIX, Windows
    :synopsis: Unit tests for po_parser

.. moduleauthor:: Oscar Campos <oscar.campos@member.fsf.org>
"""

import unittest
from os.path import dirname

from glosarium.po_parser import PoParser


class PoParserTest(unittest.TestCase):

    def setUp(self):
        self.file = '{}/test_language.po'.format(dirname(__file__))

    def test_parser_dont_read_notes_from_file(self):
        parser = PoParser(None, self.file)
        with open(self.file, 'r') as file_descriptor:
            lines = file_descriptor.readlines()

        self.assertNotEqual(len(lines), len(parser._load_file()))

    def test_result_has_no_href_src_or_hash(self):
        terms = ('webmaster')
        parser = PoParser(terms, self.file)
        result, resume = parser.parse()

        for line in result:
            if terms[0] in line.lower():
                self.assertFalse('href' in line.lower())
                self.assertFalse('src' in line.lower())
                self.assertFalse('#' in line.lower())
