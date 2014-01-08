#!/usr/bin/env python

from RibParser import RibDump
from optparse import OptionParser
from pybgpdump import BGPDump

from os import listdir
from os.path import isfile, join

resourcesPath="../../resources/"
bgpUpdatesPath = resourcesPath + "updates/"

ribFilePath = resourcesPath + "ribs/rib.20020101.0027.parsed"
prefixUpdateCount = {}


def ribPreProccess():
    counter = 0
    try:
        rib = RibDump(ribFilePath)
        for time, ip_from, as_from, prefix, aspath, next_hop in rib:
            prefixUpdateCount[prefix] = 0
            counter += 1

        print "Number of prefixes in the rib: "
        print prefixUpdateCount.__sizeof__()


    except MemoryError:
        print "Memory Error - how big is your rib ???"


def main():

    #Reading Rib file
   # ribPreProccess()

    #Reading BGP update massages

    bgpFiles = [ f for f in listdir(bgpUpdatesPath) if isfile(join(bgpUpdatesPath,f)) ]
    for filePath in bgpFiles:
        parser = OptionParser()
        parser.add_option('-i', '--input', dest='input', default=bgpUpdatesPath+filePath,
                          help='read input from FILE', metavar='FILE')
        (options, args) = parser.parse_args()

        dump = BGPDump(bgpUpdatesPath+filePath)
        for mrt_h, bgp_h, bgp_m in dump:
            print bgp_m.update.announced
            print bgp_m.update.withdrawn



if __name__ == '__main__':
    main()