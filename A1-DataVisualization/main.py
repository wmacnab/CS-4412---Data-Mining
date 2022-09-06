import csv
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()

"""
csvfile = open('data_date.csv')
reader = csv.reader(csvfile)
for i in reader:
    print(i)
"""

"""
with open('data_date.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
"""

"""
csvfile = open('data_date.csv')
list = csvfile.readline()
print(list)
"""