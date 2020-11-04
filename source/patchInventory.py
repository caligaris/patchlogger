#!/usr/bin/env python
# MIT License

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE

import subprocess
import re
import logging
import time

class Log:
    logger = logging.getLogger('patchInventory')
    hdlr = logging.FileHandler('/opt/patchlogger/patchInventory.log')
    formatter = logging.Formatter('%(asctime)s %(message)s')
    formatter.converter = time.gmtime # set timezone to GMT/UTC
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.INFO)
    
    def write(self, line):
        self.logger.info(line)

# variables
updates_list = []
logger = Log()

# run apt-get -q update &> /dev/null under protected sudo 
updateAptCmd = 'sudo /opt/patchlogger/APTUpdates.sh'
subprocess.call(updateAptCmd, shell=True)
# use apt-get to get list of packages
cmd = 'LANG=en_US.UTF8 apt-get -s dist-upgrade | grep "^Inst"'
process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
out, err = process.communicate()

# parse result of apt-get with regex
srch_txt = r'Inst[ ](.*?)[ ].*?[(](.*?)[ ](.*?)[ ]\[(.*?)\]'
srch = re.compile(srch_txt, re.M | re.S)
pkg_list = srch.findall(out)

for pkg in pkg_list:
    line = "Name=" + pkg[0] + " Architecture=" + pkg[3] + " Version=" + pkg[1] + " Repository=" + pkg[2]
    updates_list.append(line)
    logger.write(line)

# remove: 
# print(updates_list)
