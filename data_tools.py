#!/usr/bin/env python3
import argparse
from read_csv import *
import data_missing_handler
import chaining_func
from functools import partial

parser = argparse.ArgumentParser(description='Data processing tools for csv file')

parser.add_argument('input_file', help='Need process csv file path')
parser.add_argument('output_file', help='Processed csv file path')
parser.add_argument('--pipe', help='algorithm will be used')

args = parser.parse_args()

print('Input file: {}'.format(args.input_file))
print('Output file: {}'.format(args.output_file))
print('Pipeline: {}'.format(args.pipe))

header, rows = getData(args.input_file)
if rows is None:
    print("Somethings wrong happened")
else:
    HANLDE_MISSING_VALUE_SERVICE = "mv"

    def classifyService(serviceString, data):
        serviceInfo = str(serviceString).split(",")
        serviceName = serviceInfo[0]
        if serviceName == HANLDE_MISSING_VALUE_SERVICE:
            return data_missing_handler.handleMissingValue(data, serviceInfo)
        
    def processService():
        serviceStrings = str(args.pipe).split("-")
        if len(serviceStrings) == 0:
            print("Have nothing to do !")
            return []
        chain = chaining_func.compose(
                partial(classifyService, serviceStrings[0]), 
                lambda rows: rows # do nothing, this act as init state
        )
        for serviceString in serviceStrings[1:]:
            chain = chaining_func.compose(
                partial(classifyService, serviceString), 
                chain
            )
        return chain(rows)

    for i in processService():
        print(i)
    print("*******************************")
    for i in rows:
        print(i)