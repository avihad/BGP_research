#!/usr/bin/env python

from RibParser import RibDump
from optparse import OptionParser
from pybgpdump import BGPDump

from os import listdir
from os.path import isfile, join
import pygal

import tarfile
from operator import itemgetter
import math

resourcesPath="../../resources/"
bgpUpdatesPath = resourcesPath + "updates/"

ribFilePath = resourcesPath + "ribs/rib.20020101.0027.parsed"
prefixUpdateCount = {}

interArrivalIntervals = []
interArrivalEvents = []

ARRIVAL_INTERVAL = 60


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

            #Used to calculate if we are in a new interval arrival
            prefixUpdateCount[prefix]["count_tmp"] = 0
            prefixUpdateCount[prefix]["first_tmp"] = float(time)
            prefixUpdateCount[prefix]["last_tmp"] = float(time)
            counter += 1

        print "Number of prefixes in the rib: "
        print prefixUpdateCount.__sizeof__()


    except MemoryError:
        print "Memory Error - how big is your rib ???"


def extractPrefixFromStr(inputString,sourceIP, timestemp):

    inputString = inputString.replace("[", "").replace("]", "").replace("RouteIPV4(", "").replace(")","").replace(" ", "")
    if (len(inputString) > 0):
        inputString = inputString.split(",")
        for prefix in inputString:
            if prefixUpdateCount.has_key(prefix):
                #Added this to the calculation with the source ip in @updateInterArrivalTime
                #if prefixUpdateCount[prefix]["first"] != prefixUpdateCount[prefix]["last"]:
                #    interArrivalIntervals.append(timestemp - prefixUpdateCount[prefix]["last"])
                prefixUpdateCount[prefix]["count"] += 1
                prefixUpdateCount[prefix]["last"] = timestemp;
            else:
                prefixUpdateCount[prefix] = {}
                prefixUpdateCount[prefix]["count"] = 1
                prefixUpdateCount[prefix]["first"] = timestemp;
                prefixUpdateCount[prefix]["last"] = timestemp;

                #Initialize also the tmp vars
                prefixUpdateCount[prefix]["count_tmp"] = 1
                prefixUpdateCount[prefix]["first_tmp"] = timestemp
                prefixUpdateCount[prefix]["last_tmp"] = timestemp

            updateInterArrivalTime(prefix,str(sourceIP),timestemp,ARRIVAL_INTERVAL )

def updateInterArrivalTime(prefix,sourceIP,timestemp,interval):
    if prefixUpdateCount[prefix].has_key(sourceIP):

        interArrivalIntervals.append(timestemp - prefixUpdateCount[prefix][sourceIP]["last"])

        if (timestemp - prefixUpdateCount[prefix][sourceIP]["first"]) > interval :
            interArrivalEvents.append((prefixUpdateCount[prefix][sourceIP]["count"], prefixUpdateCount[prefix][sourceIP]["first"], prefixUpdateCount[prefix][sourceIP]["last"]))
            prefixUpdateCount[prefix][sourceIP]["count"] = 1
            prefixUpdateCount[prefix][sourceIP]["first"] = timestemp
            prefixUpdateCount[prefix][sourceIP]["last"] = timestemp
        else:
            prefixUpdateCount[prefix][sourceIP]["count"] += 1
            prefixUpdateCount[prefix][sourceIP]["last"] = timestemp
    else:
        prefixUpdateCount[prefix][sourceIP]= {}
        prefixUpdateCount[prefix][sourceIP]["count"] = 1
        prefixUpdateCount[prefix][sourceIP]["first"] = timestemp
        prefixUpdateCount[prefix][sourceIP]["last"] = timestemp



def interArrivalChart(values):
    interArrival = {}

    for value in values:
        timeDiff = math.floor(value)
        if interArrival.has_key(timeDiff):
            interArrival[timeDiff] +=1
        else:
            interArrival[timeDiff] = 0

    interArrivalList = [value for value in interArrival.items() if value[1] > 0 and value[0] <  100]
    interArrivalList.sort(key=itemgetter(0))

    print [value for value in interArrival.items() if value[1] == 1196]
    bar_chart = pygal.XY(title = "Inter Arrival time" , x_title = "Mili Seconds", y_title = "Num of msg in x interval in mili sec")
    bar_chart.add("Values",interArrivalList)
    bar_chart.render_to_file("interArrival.svg")



def cumulativeChart(values):

    values.sort(key=itemgetter("count"),reverse=True)
    cumulativeValues = [(0.0, values.pop(0)["count"])]

    i = 1
    values_len = len(values) * 1.0
    for value in values:
        cumulativeValues.append(((i / values_len) * 100,cumulativeValues[i - 1][1] + value["count"]))
        i += 1

    xy_chart = pygal.XY(title = "Cumulative chart", x_title = "% of prefixes", y_title="Number of update msgs")
    xy_chart.add("Values",cumulativeValues)
    xy_chart.render_to_file("cumulative.svg")

def eventUpdateCountDist(inputEvents):
    updateCount = {}
    counter = 0.0

    for event in inputEvents:
        if updateCount.has_key(event[0]):
            updateCount[event[0]] += 1
        else:
            updateCount[event[0]] = 1
        counter += 1
    updateCount = [(k,v/counter) for k , v in updateCount.items() ]

    chart = pygal.XY(title = "Update msg per event distribution", x_title="Number of update msg", y_title="Probability")
    chart.add("values",updateCount)
    chart.render_to_file("updateMsgDist.svg")

def eventDuarationDist(inputEvents):
    updateCount = {}
    counter = 0.0

    for event in inputEvents:
        key = math.floor(event[2] - event[1])
        if updateCount.has_key(key):
            updateCount[key] += 1
        else:
            updateCount[key] = 1
        counter += 1
    updateCount = [(k,v/counter) for k , v in updateCount.items() ]

    chart = pygal.XY(title = "Event duration distribution", x_title="Event duration in mili sec", y_title="Probability")
    chart.add("values",updateCount)
    chart.render_to_file("eventDurationDist.svg")

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
            sourceIP = bgp_h.src_ip
            timestemp = mrt_h.ts
            extractPrefixFromStr(str(bgp_m.update.announced),sourceIP,timestemp)
            extractPrefixFromStr(str(bgp_m.update.withdrawn),sourceIP,timestemp)

        #print("Prefix list length: ",len(prefixUpdateCount)," File name: ",filePath)

    updatedPrefixes = {k: v for k, v in prefixUpdateCount.iteritems() if v["count"] > 0}

    #Question 1.a
    print("% of prefixes with no updates: ",((1 - ((len(updatedPrefixes) * 1.0) / len(prefixUpdateCount))) * 100))

    #Question 1.b
    prefixMaxUpdates = max(prefixUpdateCount,key= lambda k: prefixUpdateCount[k]["count"])
    frequency = (prefixUpdateCount[prefixMaxUpdates]["count"]) / ((prefixUpdateCount[prefixMaxUpdates]["last"] - prefixUpdateCount[prefixMaxUpdates]["first"]) / 1000);
    print("Prefix with most updates: ",prefixMaxUpdates," Num of Updates: " ,prefixUpdateCount[prefixMaxUpdates]["count"]," Friquency: ", frequency)

    #Question 1.c
    prefixStat = prefixUpdateCount.values()
    cumulativeChart(prefixStat)

    #Question 2.a
    interArrivalChart(interArrivalIntervals)

    #Question 2.b
    print "Resalable T can be 60 mili sec as we can see from the inter arrival chart"

    #Question 2.c.i
    eventUpdateCountDist(interArrivalEvents)

    #Question 2.c.ii
    eventDuarationDist(interArrivalEvents)


if __name__ == '__main__':
    main()