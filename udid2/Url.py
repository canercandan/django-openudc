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

import pycurl
import StringIO

class Url:
    def __init__(self, url='http://localhost'):
        self.url = pycurl.Curl()
        self.url.setopt(pycurl.URL, url)
        self.out = StringIO.StringIO()
        self.url.setopt(pycurl.WRITEFUNCTION, self.out.write)
        self.url.setopt(pycurl.NOPROGRESS, 0)
        self.url.setopt(pycurl.PROGRESSFUNCTION, self.progress)

    def pre(self):
        # Not implemented, to inheritate
        pass

    def post(self):
        # Not implemented, to inheritate
        pass

    def progress(self, download_t, download_d, upload_t, upload_d):
        # print "Total to download", download_t
        # print "Total downloaded", download_d
        # print "Total to upload", upload_t
        # print "Total uploaded", upload_d
        pass

    def __call__(self):
        self.pre()
        self.url.perform()
        self.post()

    def value(self):
        return self.getvalue()

class GET(Url):
    def __init__(self, url='http://localhost'):
        Url.__init__(self, url)

class POST(Url):
    def __init__(self, url='http://localhost'):
        Url.__init__(self, url)

    def pre(self):
        #self.url.set_opt(
        pass
