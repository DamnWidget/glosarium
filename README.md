glosarium
=========

This is a cross-platform application used by the Spanish Transalation Team of
the GNU Project. It was written by Oscar Campos <oscar.campos@member.fsf.org>
and released under the GNU General Public License, version 3 or later.

This document applies to the use of glosarium on all distributions of the
GNU Operating System.


Dependencies
------------

  * Python >= 2.6
  * httplib2 >= 0.6
  * coreutils >= 8.5
  * setuptools >= 0.6 (just for be able to run python setup.py install)

**NOTE**: In debian and derivates (Ubuntu, Mint, Trisquel, etc) setuptools is named as `python-setuptools`


Instalation
-----------

Install with pip:

    $ sudo pip install glosarium

You can also donwload or clone the repository and install like any other Python package with:

    $ sudo python setup.py install


Usage
-----

Make sure you are connected to the internet (glosarium checks
http://www.gnu.org/server/standards/translations/es/recursos.html#glosario
for coincidences.)

In the command line, type:

    $ glosarium path-to-your-po-file/name_of_article.es.po  log_file

`log_file` is the file where the results will be saved. If you don't
specify it, the results will be printed on the default output, and not saved in the file system.

Options
-------

    -h, --help     show this help message and exit
    -v, --version  show program's version number and exit
    -l, --lines    also print lines when a term is found
    -r, --resume   print a resume when done

Examples
--------

The following prints a list of terms found and the number of the line where
they occur in the PO file:

    $ glosarium Desktop/tests/why-copyleft.es.po

    Term Copyleft found in line 1
    Term Free software found in line 2
    Term Copyleft found in line 8
    Term Copyleft found in line 20
    Term Free software found in line 20
    Term Free Software Foundation (FSF) found in line 20
    Term GNU Project found in line 20
    Term Copyleft found in line 21
    Term Copyleft found in line 24
    Term Copyleft found in line 25
    Term Copyleft found in line 32
    Term Copyleft license found in line 32
    Term Free software found in line 32
    Term Free software license found in line 32
    Term GNU Project found in line 32
    Term Non-copyleft license found in line 32
    Term Copyleft found in line 33
    Term Free software found in line 40
    Term Free software license found in line 40
    Term Copyleft found in line 44
    Term Copyleft license found in line 44
    Term Free software found in line 44
    Term Non-copyleft license found in line 44
    Term Copyleft found in line 45
    Term Webmaster found in line 57
    Term Webmaster found in line 58
    Term See found in line 62
    Term Free software found in line 66
    Term Free software found in line 67

The following prints same as above, plus statistics (resume):

    $ glosarium -r Desktop/tests/why-copyleft.es.po

    +-----------------------------------------------------------------------------+
    | Term                          | Appears in lines                            |
    +-----------------------------------------------------------------------------+
    | Free Software Foundation (FSF)| [20]                                        |
    | Free software                 | [2, 20, 32, 40, 44, 66, 67]                 |
    | Copyleft                      | [1, 8, 20, 21, 24, 25, 32, 33, 44, 45]      |
    | GNU Project                   | [20, 32]                                    |
    | See                           | [62]                                        |
    | Non-copyleft license          | [32, 44]                                    |
    | Free software license         | [32, 40]                                    |
    | Copyleft license              | [32, 44]                                    |
    | Webmaster                     | [57, 58]                                    |
    +-----------------------------------------------------------------------------+
    | Total 9 terms                                                               |
    +-----------------------------------------------------------------------------+

The following prints the context where the term occurs:

    $ glosarium -l Desktop/tests/why-copyleft.es.po

    Term Copyleft found in line 32<br />
    |__<br />
      msgid "In the GNU Project we usually recommend people use
      <a href=\"/copyleft/copyleft.html\">copyleft</a> licenses like GNU GPL, rather
      than permissive non-copyleft free software licenses.  We don't argue harshly
      against the non-copyleft licenses&mdash;in fact, we occasionally recommend
      them in special circumstances&mdash;but the advocates of those licenses show a
      pattern of arguing harshly against the
      <acronym title=\"General Public License\">GPL</acronym>."

Common Troubleshooting
----------------------

* Q: When I use the `glosarium` command I get `command not found` error. What can I do?
* R: Install the coreutils from the GNU project


License:
--------
    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
