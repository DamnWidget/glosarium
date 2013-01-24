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
    :synopsis: This module loads glosary terms from a formatted web page

.. moduleauthor:: Oscar Campos <oscar.campos@member.fsf.org>
"""

import re
import httplib2


class WebParserError(Exception):
    """Class for WebParser exceptions
    """


class WebParser(object):
    """
    This class is used to parse the Glosarium GNU web page and generates a
    list of terms to use in our glosary

    :param url: the URL to parse
    :type url: str
    """

    def __init__(self, url=None):
        if url is None:
            self.url = (
                'http://www.gnu.org/server/standards/translations/es/'
                'recursos.html#glosario'
            )
        self.__glosary = {}
        self._parsed = False

    @property
    def glosary(self):
        """Return the glosary back
        """
        if not self._parsed:
            self._parse()

        return self.__glosary

    def _parse(self):
        """I parse the web site
        """

        h = httplib2.Http('/tmp/.cache')
        try:
            resp, content = h.request(self.url)
            content = '\n'.join(content.split('\n')[
                content.split('\n').index('<!-- Begin Glosario -->') + 1:
                content.split('\n').index('<!-- End Glosario -->')
            ])
        except httplib2.ServerNotFoundError:
            raise WebParserError(
                'GNU site is unavailable, check your internet connection'
            )

        if resp.get('status') != '200':
            raise WebParserError('error: the server at {0} reply {1}'.format(
                self.url, resp.get('status')
            ))

        regex = re.compile(r'(?<=<strong>)(?P<term>.*?)(?=</strong>)')
        regex2 = re.compile(
            r'((?<=</strong>\:)[\s\S]*?(?=<strong>|<br />|</p>))')
        terms = [term.strip('"') for term in regex.findall(content)]
        translations = [
            re.sub(r'<[^<]+?>', '', term).strip()
            for term in regex2.findall(content)
        ]
        self.__glosary = dict(zip(terms, translations))
        self._parsed = True


__all__ = ['WebParser', 'WebParserError']
