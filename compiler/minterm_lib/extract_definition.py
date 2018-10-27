#!/usr/bin/python

import sys

if len(sys.argv) < 2 :
    print "need spec name"
    exit(-1)

filename = sys.argv[1]

def parse_line(line):
    line = line.strip()
    if str.startswith(line,"int"):
        varnames = line[4:].split(",")
        return "int",varnames 
    elif str.startswith(line,"IP"):
        varnames = line[3:].split(",")
        return "IP",varnames
    elif str.startswith(line,"bool"):
        varnames = line[5:].split(",")
        return "bool",varnames


def get_variables():
    builtin = ['ethDst','ethSrc','ethType','ip4Src','ip4Dst','Port','ipProto','port_id']
    res = dict()
    res["int"] = list()
    res["IP"] = list()
    res["bool"] = list()


    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            typ,varnames = parse_line(line)
            print typ,varnames
            for var in varnames:
                if var in builtin:
                    print "Error !!! redeclaring a builtin variable"
                res[typ].append(var)
    return res
