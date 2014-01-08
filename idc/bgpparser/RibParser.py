#!/usr/bin/env python

class RibDump:
    def __init__(self, filename):
        self.f = file(filename, 'rb')

    def open(self, filename):
        self.f = file(filename, 'rb')

    def close(self):
        self.f.close()
        raise StopIteration

    def __iter__(self):
        return self

    def next(self):
        line = self.f.readline()
        if(line.__len__() == 0):
            self.close()

        split = line.split("|")
        time = split[1]
        ip_from = split[3]
        as_from = split[4]
        prefix = split[5]
        aspath = split[6]
        next_hop = split[8]

        return (time,ip_from,as_from,prefix,aspath,next_hop)

