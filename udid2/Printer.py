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
    """Base printer class to select the key parameters to return with KeysLoader"""

    def __call__(self, key, fpr0, uid):
        raise ValueError('Have to be inheritated from a keys printer subclass.')

class Default(Keys):
    def __call__(self, key, fpr0, uid):
        return fpr0, uid.uid

class Fingerprint(Keys):
    def __call__(self, key, fpr0, uid):
        return fpr0

class AllData(Keys):
    def __call__(self, key, fpr0, uid):
        return fpr0, uid.name, uid.comment, uid.email
