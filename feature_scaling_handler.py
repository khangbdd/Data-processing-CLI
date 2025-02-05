import math

def _normalize(featureData):
    floatFeatureData = [float(value) for value in featureData]
    minValue = min(floatFeatureData)
    maxValue = max(floatFeatureData)
    return map(lambda value: (value - minValue)/(maxValue - minValue), floatFeatureData)

def _standardize(featureData):
    floatFeatureData = [float(value) for value in featureData]
    size = len(floatFeatureData)
    sumValue = sum(floatFeatureData)
    mean = sumValue/size
    std = math.sqrt(sum([(value - mean)**2 for value in floatFeatureData])/(size - 1))
    return map(lambda value: (value - mean)/std, floatFeatureData)

def scaleWithSomeFeatureOnly(action, header, featuresData, features):
    def scaleIfNeed(index, value):
        if header[index] in features:
            return action(value)
        else:
            return value
    return [scaleIfNeed(index, value) for index, value in enumerate(featuresData)]

def transpose(lst): return list(map(list, zip(*lst)))

NORMALIZATION = "nm"
STANDARDIZATION = "sd"
def featureScale(header, rows, serviceInfo):
    subserviceInfo = serviceInfo[1].split("_")
    subserviceName = subserviceInfo[0]
    features = subserviceInfo[1:]
    featuresData = transpose(rows)
    if subserviceName == NORMALIZATION:
        if features == []:
            return transpose(list(map(_normalize, featuresData)))
        else:
            return transpose(scaleWithSomeFeatureOnly(_normalize, header, featuresData, features))
    if subserviceName == STANDARDIZATION:
        if features == []:
            return transpose(list(map(_standardize, featuresData)))
        else:
            return transpose(scaleWithSomeFeatureOnly(_standardize, header, featuresData, features))
    print("Service {} is invalid, go on with normalization".format(subserviceName))
    return map(_normalize, featuresData)