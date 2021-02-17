#!/usr/bin/env python

# This file is part of DSX, development environment for static SoC
# applications.

# This file is distributed under the terms of the GNU General Public
# License.


import dsx
from dsx import *
from soclib import *

tcg = dsx.Tcg(dsx.Task('hello', "hello"))


tcg.generate( dsx.Posix() )
