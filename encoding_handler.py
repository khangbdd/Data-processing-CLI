from utils import transpose

def _gatherTypeForOnehot(featureData):
    dictionaryOfType = {}
    index = 0
    for value in featureData:
        existData = dictionaryOfType.get(value, -1)
        if existData == -1:
            dictionaryOfType[value] = index
            index += 1
    return dictionaryOfType

def _onehotEncoding(featureData): 
    dictionaryOfType = _gatherTypeForOnehot(featureData)
    size = len(dictionaryOfType)
    def toList(index):
        list = [0]*size
        list[index] = 1
        return list
    return [toList(dictionaryOfType[value]) for value in featureData]
    
def _ordinalEncoding(featureData):
    dictionaryOfType = {}
    count = 0
    encodedList = [0]*len(featureData)
    for index, value in enumerate(featureData):
        existData = dictionaryOfType.get(value, -1)
        if existData == -1:
            dictionaryOfType[value] = count
            encodedList[index] = count
            count += 1
        else:
            encodedList[index] = existData
    return encodedList

def _encodeWithSelectedFeature(action, header, featuresData, features):
    def encodeIfNeed(index, value):
        if header[index] in features:
            return action(value)
        else:
            return value
    return [encodeIfNeed(index, value) for index, value in enumerate(featuresData)]

ONEHOT_ENCODING = "oh"
ORDINAL_ENCODING = "od"
def handleEncoding(header, rows, serviceInfo):
    subserviceInfo = serviceInfo[1].split("_")
    subserviceName = subserviceInfo[0]
    features = subserviceInfo[1:]
    featuresData = transpose(rows)
    if features == []:
        raise Exception("You need to input the feature name that need to encode")
    if subserviceName == ONEHOT_ENCODING:
        return transpose(_encodeWithSelectedFeature(_onehotEncoding, header, featuresData, features))
    if subserviceName == ORDINAL_ENCODING:
        return transpose(_encodeWithSelectedFeature(_ordinalEncoding, header, featuresData, features))
    print("Service {} is invalid, go on with one-hot encoding.".format(subserviceName))
    return transpose(_encodeWithSelectedFeature(_onehotEncoding, header, featuresData, features))
