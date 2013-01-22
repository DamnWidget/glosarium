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


Usage
-----

Place a copy of the file "glosarium" in your /home directory.

Make sure you are connected to the internet (glosarium checks 
http://www.gnu.org/server/standards/translations/es/recursos.html#glosario
for coincidences.)

In the command line, type:

    $ python ./glosarium path-to-your-po-file/name_of_article.es.po  log_file

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

    $ python ./glosarium Desktop/tests/why-copyleft.es.po

    Term Copyleft found in line 1<br />
    Term Free software found in line 2<br />
    Term Copyleft found in line 8<br />
    Term Copyleft found in line 20<br />
    Term Free software found in line 20<br />
    Term Free Software Foundation (FSF) found in line 20<br />
    Term GNU Project found in line 20<br />
    Term Copyleft found in line 21<br />
    Term Copyleft found in line 24<br />
    Term Copyleft found in line 25<br />
    Term Copyleft found in line 32<br />
    Term Copyleft license found in line 32<br />
    Term Free software found in line 32<br />
    Term Free software license found in line 32<br />
    Term GNU Project found in line 32<br />
    Term Non-copyleft license found in line 32<br />
    Term Copyleft found in line 33<br />
    Term Free software found in line 40<br />
    Term Free software license found in line 40<br />
    Term Copyleft found in line 44<br />
    Term Copyleft license found in line 44<br />
    Term Free software found in line 44<br />
    Term Non-copyleft license found in line 44<br />
    Term Copyleft found in line 45<br />
    Term Webmaster found in line 57<br />
    Term Webmaster found in line 58<br />
    Term See found in line 62<br />
    Term Free software found in line 66<br />
    Term Free software found in line 67<br />

The following prints same as above, plus statistics (resume): 

    $ python ./glosarium -r Desktop/tests/why-copyleft.es.po

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

    $ python ./glosarium -l Desktop/tests/why-copyleft.es.po

    Term Copyleft found in line 32<br />
    |__<br />
      msgid "In the GNU Project we usually recommend people use 
      <a href=\"/copyleft/copyleft.html\">copyleft</a> licenses like GNU GPL, rather 
      than permissive non-copyleft free software licenses.  We don't argue harshly 
      against the non-copyleft licenses&mdash;in fact, we occasionally recommend 
      them in special circumstances&mdash;but the advocates of those licenses show a 
      pattern of arguing harshly against the 
      <acronym title=\"General Public License\">GPL</acronym>."

You can ofcourse copy glosarium script to your `$PATH` so you can use it as:

    $ glosarium imput_file output_file
    
License:
--------
    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
