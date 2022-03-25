import glob
from csv import reader
import pandas as pd
import os

global b

def credings():
    # get data file names
    pathf = (os.getcwd() + '/backend/Csv_files')
    filenames = glob.glob(pathf + "/*.csv")

    map={}

    dfs = []
    for filename in filenames:
        dfs.append(pd.read_csv(filename))
        with open(filename, 'r') as read_obj:
            # pass the file object to reader() to get the reader object
            csv_reader = reader(read_obj, delimiter=" ")
            # Iterate over each row in the csv using reader object
            for line in csv_reader:
                # row variable is a list that represents a row in csv
                if(line[0]=="Name:"):
                    a=line[1]

                if line[0] == "Cost:":
                    b=line[1]


                if a in map:
                    c=map.pop(a)
                    c=b+c
                    map[a]=c
                else:
                    map[a]=b


    print(map)