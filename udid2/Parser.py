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

"""
The Parser class is used to parse keys loaded from the keys loader class.
"""

import Loader as l, Printer as pr

class Keys:
    """Parse keys from keys loader"""

    def __init__(self, loader=l.Keys()):
        self.loader = loader

    def __call__(self):
        for fields in self.loader():
            yield self.call(fields)

    def call(self, fields):
        raise ValueError('Have to be inheritated from a keys parser subclass.')

class Fingerprint(Keys):
    def __init__(self, loader=l.Keys(printer=pr.Fingerprint())):
        Keys.__init__(self, loader)

    def call(self, fields):
        d = {}
        d['fingerprint'] = fields
        return d

class AllData(Keys):
    def __init__(self, loader=l.Keys(printer=pr.AllData())):
        Keys.__init__(self, loader)

    def call(self, fields):
        d = {}
        #print fields[:4]
        d['fingerprint'], d['name'], d['comment'], d['email'] = fields[:4]
        return d
