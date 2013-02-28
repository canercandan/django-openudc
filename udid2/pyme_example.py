#!/usr/bin/env python2

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

import sys
from pyme import core, constants

# # Set up our input and output buffers.

# plain = core.Data('This is my message.')
# cipher = core.Data()

# # Initialize our context.

# c = core.Context()
# c.set_armor(1)

# # Set up the recipients.

# sys.stdout.write("Enter name of your recipient: ")
# name = sys.stdin.readline().strip()
# c.op_keylist_start(name, 0)
# r = c.op_keylist_next()

# # Do the encryption.

# c.op_encrypt([r], 1, plain, cipher)
# cipher.seek(0,0)
# print cipher.read()

c = core.Context()
for key in c.op_keylist_all(None, False):
    print 'key(%s)' % key.subkeys[0].fpr
    for uid in key.uids:
        print '\t%s' % uid.uid
