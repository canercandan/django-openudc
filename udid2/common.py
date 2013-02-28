#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2
# as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
#
# Authors:
# Caner Candan <caner@candan.fr>, http://caner.candan.fr
#

"""
How to use the program parsing and logging features ?

(1) Add at the header of your program the following lines:

import optparse, logging
import common

(2) Define a logging context:

logger = logging.getLogger("YOUR_PROGRAM")

(3) Define the options parser:

options = common.parser()

(3bis) You can also define your own options:

parser = optparse.OptionParser()
parser.add_option('-f', '--filename', help='give a filename')
options = common.parser(parser)
"""

import optparse, logging, sys

LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL}

def parser(parser=optparse.OptionParser()):
    parser.add_option('-v', '--verbose', choices=LEVELS.keys(), default='info', help='set a verbose level')
    parser.add_option('-l', '--levels', action='store_true', default=False, help='list verbose levels')
    parser.add_option('-o', '--output', help='give an output filename for logging', default='')

    options, args = parser.parse_args()
    if options.levels: list_verbose_levels()
    logger(options.verbose, options.output)
    return options

def logger(level_name, filename=''):
    if (filename != ''):
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
            filename=filename, filemode='a'
            )
        return

    logging.basicConfig(
        level=LEVELS.get(level_name, logging.NOTSET),
        format='%(name)-12s: %(levelname)-8s %(message)s'
        )

def list_verbose_levels():
    print "Here's the verbose levels available:"
    for keys in LEVELS.keys():
        print "\t", keys
    sys.exit()
