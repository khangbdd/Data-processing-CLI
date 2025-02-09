def _remove(rows): return filter(lambda row: ('' not in row) and (None not in row), rows)

def _fillWithValue(rows, defaultValue):
    def choose(value):
        if (value is '') or (value is None):
            return defaultValue
        else:
            return value
    def fill(row): return [choose(value) for value in row]
    return [fill(row) for row in rows]

REMOVING = "rm"
FILLING = "fl"
def handleMissingValue(rows, serviceInfo):
    subserviceInfo = serviceInfo[1].split("_")
    subserviceName = subserviceInfo[0]
    if subserviceName == REMOVING:
        return _remove(rows)
    if subserviceName == FILLING:
        try:
            defaultValue = int(subserviceInfo[1])
            return _fillWithValue(rows, defaultValue)
        except:
            print("Your default value is invalid, go on with defaultValue 0")
            return _fillWithValue(rows, 0)
    print("Service {} is invalid, go on with removing".format(subserviceName))
    return _remove(rows)