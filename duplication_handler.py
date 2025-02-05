def removeDuplication(rows):
    dictionary = {}
    results_rows = []
    for row in rows:
        key = str(row)
        if dictionary.get(key, False) == False:
            results_rows.append(row)
        dictionary[key] = True
    return results_rows

            


    