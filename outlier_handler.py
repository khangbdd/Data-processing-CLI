import math
from utils import transpose
from functools import partial

Z_THRESHOLD = [-3, 3]
z_score = lambda diff, std: diff/std
def _isAValueOutlier(value, mean, std):
    score = z_score(float(value) - mean, std)
    return score < Z_THRESHOLD[0] or score > Z_THRESHOLD[1]

def _precalculateForFeature(featureData):
    floatFeatureData = [float(value) for value in featureData]
    size = len(floatFeatureData)
    mean = sum(floatFeatureData)/size
    std = math.sqrt(sum((value - mean)**2 for value in floatFeatureData)/(size - 1))
    return mean, std

def _precalculateForNeededFeatures(header, featuresData, features):
    dictionary = {}
    for index, item in enumerate(header):
        if item in features:
            dictionary[item] = _precalculateForFeature(featuresData[index])
    return dictionary

def _isARowNotOutlier(precalculatedDict, header, row):
    for index, value in enumerate(row):
        key = header[index]
        precalculate = precalculatedDict.get(key, False)
        if precalculate != False:
            mean, std = precalculate
            if _isAValueOutlier(value, mean, std):
                return False
    return True

def _replacingOulier(index, value, precalculatedDict, header):
    key = header[index]
    precalculate = precalculatedDict.get(key, False)
    if precalculate != False:
        mean, std = precalculate
        score = z_score(float(value) - mean, std)
        print(score)
        if score < Z_THRESHOLD[0]: 
            return mean - 3 * std
        elif score > Z_THRESHOLD[1]:
            return mean + 3 * std
    return value

REMOVING = "rm"
REPLACING = "rp"
def handleOutlier(header, rows, serviceInfo):
    subserviceInfo = serviceInfo[1].split("_")
    subserviceName = subserviceInfo[0]
    features = subserviceInfo[1:]
    featuresData = transpose(rows)
    precalculatedDict = {}
    if features == []:
        precalculatedDict = _precalculateForNeededFeatures(header, featuresData, header)
    else:
        precalculatedDict = _precalculateForNeededFeatures(header, featuresData, features)
    removedOutlier = filter(partial(_isARowNotOutlier,precalculatedDict, header), rows)
    if subserviceName == REMOVING:
        return filter(partial(_isARowNotOutlier,precalculatedDict, header), rows)
    if subserviceName == REPLACING:
        precalculatedDict
        return [[_replacingOulier(index, value, precalculatedDict, header) for index, value in enumerate(row)] for row in rows]
    print("Service {} is invalid, go on with replacing.".format(subserviceName))
    return [[_replacingOulier(index, value, precalculatedDict, header) for index, value in enumerate(row)] for row in rows]