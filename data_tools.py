#!/usr/bin/env python3
import argparse
from read_csv import *
import data_missing_handler
import duplication_handler
import feature_scaling_handler
import outlier_handler
import encoding_handler
from utils import compose
from functools import partial
from save_csv import *

parser = argparse.ArgumentParser(description='Data processing tools for csv file')

parser.add_argument('input_file', help='Need process csv file path')
parser.add_argument('output_path', help='Processed csv file path')
parser.add_argument('--pipe', help='algorithm will be used')

args = parser.parse_args()

print('Input file: {}'.format(args.input_file))
print('Output file: {}'.format(args.output_path))
print('Pipeline: {}'.format(args.pipe))

header, rows = getData(args.input_file)
if rows is None:
    print("Somethings wrong happened")
else:
    HANDLE_MISSING_VALUE_SERVICE = "mv"
    HANDLE_DUPLICATED_VALUE_SERVICE = "dp"
    HANDLE_FEATURE_SCALING_SERVICE = "fs"
    HANDLE_OUTLIER_SERVICE = "ol"
    HANDLE_ENCODING_SERVICE = "ec"
    def classifyService(serviceString, data):
        serviceInfo = str(serviceString).split(",")
        serviceName = serviceInfo[0]
        if serviceName == HANDLE_MISSING_VALUE_SERVICE:
            return data_missing_handler.handleMissingValue(data, serviceInfo)
        if serviceName == HANDLE_DUPLICATED_VALUE_SERVICE:
            return duplication_handler.removeDuplication(data)
        if serviceName == HANDLE_FEATURE_SCALING_SERVICE:
            return feature_scaling_handler.featureScale(header, data, serviceInfo)
        if serviceName == HANDLE_OUTLIER_SERVICE:
            return outlier_handler.handleOutlier(header, data, serviceInfo)
        if serviceName == HANDLE_ENCODING_SERVICE:
            return encoding_handler.handleEncoding(header, data, serviceInfo)
    def processService():
        serviceStrings = str(args.pipe).split("-")
        if len(serviceStrings) == 0:
            print("Have nothing to do !")
            return []
        chain = compose(
                partial(classifyService, serviceStrings[0]), 
                lambda rows: rows # do nothing, this act as init state
        )
        for serviceString in serviceStrings[1:]:
            chain = compose(
                partial(classifyService, serviceString), 
                chain
            )
        return chain(rows)
    
    for i in processService():
        print(list(i))
    print("*******************************")
    for i in rows:
        print(i)
    saveProgressedData(args.output_path, header, list(processService()))