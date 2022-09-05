# Storing Data to CSV (comma-separated values) (popular to store spreadsheet data)

# example:

# fruit,cost
# apple,1.00
# banana,0.30
# pear,1.25

# if downloading CSV files directly without any parsing/modification, this section isn't needed

# Modifying a CSV file, or even creating one entirely from scratch, is extremely easy with Python's csv library

import csv

csvFile = open('test.csv', 'w+')
try:
    writer = csv.writer(csvFile)
    writer.writerow(('number', 'number plus 2', 'number times 2'))
    for i in range(10):
        writer.writerow((i, i+2, i*2))
finally:
    csvFile.close()


