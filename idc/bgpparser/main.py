#!/usr/bin/env python

from RibParser import RibDump
from optparse import OptionParser
from pybgpdump import BGPDump

from os import listdir
from os.path import isfile, join
import pygal

import tarfile
from operator import itemgetter

resourcesPath="../../resources/"
bgpUpdatesPath = resourcesPath + "updates/"

ribFilePath = resourcesPath + "ribs/rib.20020101.0027.parsed"
prefixUpdateCount = {}


def ribPreProccess():
    tfile = tarfile.open(ribFilePath+".tar.gz","r:gz")
    tfile.extractall(resourcesPath+"ribs/")
    counter = 0
    try:
        rib = RibDump(ribFilePath)
        for time, ip_from, as_from, prefix, aspath, next_hop in rib:
            prefixUpdateCount[prefix] = {}
            prefixUpdateCount[prefix]["count"] = 0
            prefixUpdateCount[prefix]["first"] = float(time)
            prefixUpdateCount[prefix]["last"] = float(time)
            counter += 1

        print "Number of prefixes in the rib: "
        print prefixUpdateCount.__sizeof__()


    except MemoryError:
        print "Memory Error - how big is your rib ???"


def extractPrefixFromStr(inputString, timestemp):

    inputString = inputString.replace("[", "").replace("]", "").replace("RouteIPV4(", "").replace(")","").replace(" ", "")
    if (len(inputString) > 0):
        inputString = inputString.split(",")
        for prefix in inputString:
            if (prefixUpdateCount.has_key(prefix)):
                prefixUpdateCount[prefix]["count"] += 1
                prefixUpdateCount[prefix]["last"] = timestemp;
            else:
                prefixUpdateCount[prefix] = {}
                prefixUpdateCount[prefix]["count"] = 1
                prefixUpdateCount[prefix]["first"] = timestemp;
                prefixUpdateCount[prefix]["last"] = timestemp;


def main():

    #Reading Rib file
    print("Prefix list length: ",len(prefixUpdateCount))
    ribPreProccess()
    print("Prefix list length: ",len(prefixUpdateCount))

    #Reading BGP update massages

    bgpFiles = [ f for f in listdir(bgpUpdatesPath) if isfile(join(bgpUpdatesPath,f)) ]
    bgpFiles = sorted(bgpFiles)
    for filePath in bgpFiles:
        parser = OptionParser()
        parser.add_option('-i', '--input', dest='input', default=bgpUpdatesPath+filePath,
                          help='read input from FILE', metavar='FILE')
        (options, args) = parser.parse_args()

        dump = BGPDump(bgpUpdatesPath+filePath)
        for mrt_h, bgp_h, bgp_m in dump:
            timestemp = mrt_h.ts
            extractPrefixFromStr(str(bgp_m.update.announced),timestemp)
            extractPrefixFromStr(str(bgp_m.update.withdrawn),timestemp)

        #print("Prefix list length: ",len(prefixUpdateCount)," File name: ",filePath)

    updatedPrefixes = {k: v for k, v in prefixUpdateCount.iteritems() if v["count"] > 0}

    #Question 1.a
    print("% of prefixes with no updates: ",((1 - ((len(updatedPrefixes) * 1.0) / len(prefixUpdateCount))) * 100))

    #Question 1.b
    prefixMaxUpdates = max(prefixUpdateCount,key= lambda k: prefixUpdateCount[k]["count"])
    frequency = (prefixUpdateCount[prefixMaxUpdates]["count"]) / ((prefixUpdateCount[prefixMaxUpdates]["last"] - prefixUpdateCount[prefixMaxUpdates]["first"]) / 1000);
    print("Prefix with most updates: ",prefixMaxUpdates," Num of Updates: " ,prefixUpdateCount[prefixMaxUpdates]["count"]," Friquency: ", frequency)

    #Question 1.c
    cumulativeChart(prefixUpdateCount.values())



def cumulativeChart(values):

    values.sort(key=itemgetter("count"),reverse=True)
    cumulativeValues = [(0.0, values.pop(0)["count"])]

    i = 1
    values_len = len(values) * 1.0
    for value in values:
        cumulativeValues.append(((i / values_len) * 100,cumulativeValues[i - 1][1] + value["count"]))
        i += 1

    xy_chart = pygal.XY()
    xy_chart.title = "Cumulative chart"
    xy_chart.add("Values",cumulativeValues)
    xy_chart.render_to_file("cumulative.svg")


if __name__ == '__main__':
    main()