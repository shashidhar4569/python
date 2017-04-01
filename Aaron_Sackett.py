# Hello shashidhar code like u never did it

# Importing required packages
import pandas as pd
import numpy as np
import csv
import re





data = pd.read_table('Aaron_sample.txt', delimiter=',', error_bad_lines=False, warn_bad_lines=True, compression='infer')
data['ElectionDescription'] = data['ElectionDescription'].str.extract('([a-zA-Z ]+$)')
data.ElectionDate = data.ElectionDate+'@'+data.ElectionDescription
data = data.drop('ElectionDescription', axis=1)
na=None
data2 = pd.DataFrame(na, index=data.VoterId.unique(), columns= data.ElectionDate.unique())
i = 0
for index,row in data.iterrows():
    data2.loc[row.values[0],row.values[1]] = row.values[2]
    i =i+1
    print(i)
data2.to_csv('finished.csv')
# list(data)
# len(data.ElectionDate.unique())
# len(data.VoterId.unique())
#data2.index.name = 'VoterId'
# Importing the dataset.
# data = open('/Users/ShashidharReddyPalle/Desktop/Aaron.txt', 'r')
# with open('/Users/ShashidharReddyPalle/Desktop/Aaron.txt',encoding='utf8') as f:
#      data = f.read()
# # Converting the third column of data. Select only character from the data avoiding dates.
# # Preparing a Dataset with from previous one.
# #
# data = np.array(data)
#
# #data = pd.read_csv('/Users/ShashidharReddyPalle/Desktop/Aaron.txt', sep=",", error_bad_lines=False)
# with open("Aaron_sample.txt", "r") as filestream:
#     with open("data2.csv", "w") as filestreamtwo:
#         for line in filestream:
#             currentline = line.split(",")
#             total = str(str(currentline[0]) + ',' + str(currentline[1].str.extract('([a-zA-Z ]+$)')) + ',' + str(currentline[2]) + ',' + str(currentline[3])) + "\n"
#             filestreamtwo.write(total)