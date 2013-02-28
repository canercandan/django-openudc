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
Udid2 package provide classes to load and format udid2 keys.

For instance:

- To load all hased udid2 secret keys you can use the following code:
import Udid2
udid2 = [x for x in Udid2.HashedVerboseParser()()]

- To load all clear udid2 secret keys then you can use the following code:
import Udid2
udid2 = [x for x in Udid2.ClearVerboseParser()()]
"""

import Printer as pr, Loader as l, Parser as pa, Finder as f

class Printer(pr.Fingerprint): pass

class VerbosePrinter(pr.AllData):
    def __call__(self, key, fpr0, uid):
        d = pr.AllData.__call__(self, key, fpr0, uid)
        return d + tuple(uid.comment.split(';')[:-1])

class Finder(f.Comment):
    """Use it to get udid2 commented keys"""

    def __init__(self, visibility='h', version=2, pattern='udid%(version)d;%(visibility)c'):
        """
        visibility: c (clear) or h (hashed)
        version: 2 (for compatibility issue)
        pattern: comment pattern used by the udid2 keys
        """

        fields = {'visibility': visibility, 'version': version}
        f.Comment.__init__(self, pattern % fields)

class Loader(l.Keys):
    """Download udid2 keys from the keyring"""

    def __init__(self, secret=True, finder=Finder(), printer=pr.Fingerprint()):
        l.Keys.__init__(self, secret=secret, finder=finder, printer=printer)

class Parser(pa.Fingerprint):
    def __init__(self, loader=Loader()):
        pa.Fingerprint.__init__(self, loader)

class VerboseParser(pa.AllData):
    def __init__(self, visibility='h'):
        pa.AllData.__init__(self, Loader(printer=VerbosePrinter(), finder=Finder(visibility=visibility)))

class HashedVerboseParser(VerboseParser):
    def __init__(self):
        VerboseParser.__init__(self, visibility='h')

    def call(self, fields):
        d = VerboseParser.call(self, fields)
        d['protocol'], d['visibility'], d['hashed'], d['increment'] = fields[4:]
        return d

class ClearVerboseParser(VerboseParser):
    def __init__(self):
        VerboseParser.__init__(self, visibility='c')

    def call(self, fields):
        d = VerboseParser.call(self, fields)
        d['protocol'], d['visibility'], d['lastname'], d['firstname'], d['birth_date'], d['birth_location'], d['increment'] = fields[4:]
        return d
