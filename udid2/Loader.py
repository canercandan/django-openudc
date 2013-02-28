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

from pyme import errors, core
from pyme.core import Context, Data, pubkey_algo_name
from pyme.constants import validity, status, keylist, sig, sigsum

import Finder, Printer

class Keys:
    """Download keys from the keyring"""

    def __init__(self, secret=False, finder=Finder.Dummy(), printer=Printer.Default()):
        self.context = core.Context()
        self.secret = secret
        self.finder = finder
        self.printer = printer

    def __call__(self):
        self.context.set_keylist_mode(keylist.mode.SIGS)
        for key in self.context.op_keylist_all(None, self.secret):
            for uid in key.uids:
                if self.finder(uid):
                    yield self.printer(key, key.subkeys[0].fpr, uid)
