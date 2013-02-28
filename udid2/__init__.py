#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors:
# Caner Candan <caner@candan.fr>, http://caner.candan.fr
#

__all__ = ['PyUDC']

__author__      = 'Caner Candan'
__version__     = '0.1'
__nonsense__    = 'OpenUDC'

import common

# class PyUDC:
#     """Main class"""

#     def __init__(self):
#         pass

# def gen_udid():
#     pass

from pprint import pprint

import Udid2, Parser

if __name__ == '__main__':
    #raise ValueError('Should be imported (import PyUDC)')
    udid2 = [x for x in Udid2.HashedVerboseParser()()]
    if not udid2:
        raise ValueError('no udid2 found with secret')

    pprint(udid2)

    #pprint( [x for x in Parser.AllData()()] )
