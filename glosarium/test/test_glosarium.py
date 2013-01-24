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
.. module:: test_glosarium
    :platform: POSIX, Windows
    :synopsis: Unit tests for glosarium

.. moduleauthor:: Oscar Campos <oscar.campos@member.fsf.org>
"""

import unittest

from glosarium import __version__ as version


class GlosariumTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_version(self):
        self.assertEqual(version, '1.2')
