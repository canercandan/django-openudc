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

class Keys:
    """Base finder class to define a few search criteria"""

    def __init__(self):
        self.finders = []

    def __call__(self, uid):
        for finder in self.finders:
            if not finder(uid):
                return False
        return self.call(uid)

    def call(self, uid):
        raise ValueError('Have to be inheritated from a keys finder subclass.')

    def add(self, finder):
        self.finders += [finder]

class Dummy(Keys):
    def call(self, uid): return True

class Name(Keys):
    """Use it to get keys with a name closed to the one given"""

    def __init__(self, name):
        Keys.__init__(self)
        self.name = name

    def call(self, uid): return self.name in uid.name

class Email(Keys):
    """Use it to get keys with an email address closed to the one given"""

    def __init__(self, email):
        Keys.__init__(self)
        self.email = email

    def call(self, uid): return self.email in uid.email

class Comment(Keys):
    """Use it to get keys with a comment closed to the one given"""

    def __init__(self, comment):
        Keys.__init__(self)
        self.comment = comment

    def call(self, uid): return self.comment in uid.comment
