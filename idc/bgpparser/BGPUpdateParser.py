__author__ = 'avihad'

import pybgpdump

bgpUpdatesPath="../../resources/updates/"
bgpFile = bgpUpdatesPath + "updates.20020101.0012.bz2"

print bgpFile

try:
    bgpDump = pybgpdump.BGPDump(bgpFile)
except IOError, e:
    print e;

try:
    while True:
        data = bgpDump.next()
        print data
except Exception, e:
    print e



