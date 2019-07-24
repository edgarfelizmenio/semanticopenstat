import csv
import os

data_files = os.path.join('data', 'raw', 'education')

filename = os.path.join(data_files, os.path.splitext(os.path.basename(__file__))[0]) + '.csv'

with open(filename) as input_file:
    stream = csv.reader(input_file)
    title = next(stream)[0]
    next(stream)
    headers = next(stream)
    for line in stream:
        print(line)
    print(title)
    print(headers)