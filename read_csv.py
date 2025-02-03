import csv

def getData(path):
    try:
        file = open(path)
        csvReader = csv.reader(file)
        full_data = [row for row in csvReader]
        header = full_data[0]
        data = full_data[1:] 
        return header, data
    except:
        print("Invalid file path")
    finally:
        file.close()