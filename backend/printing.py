import glob
from csv import reader
import pandas as pd
from Csv_files import *

path='backend/Csv_files'
all_files= glob.glob(path + '/*.csv')
all_files

def reader():
    # open file in read mode
    with open('/home/al3x4ndru1/PycharmProjects/Lucia/Csv_files/Production_2022-03-22 13:22:55.134930.csv', 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj, delimiter=" ")
        # Iterate over each row in the csv using reader object
        for line in csv_reader:
            # row variable is a list that represents a row in csv
            print(line)