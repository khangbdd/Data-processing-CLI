import csv
import time

def saveProgressedData(path, header, data):
    filePath = "{}/{}.csv".format(path, time.time_ns())
    with open(filePath, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)