from pathlib import Path
import csv
import pandas as pd
import operator
import collections


data_folder = Path('C:/Users/sscot/Dropbox (SRCMLLC)/SRCM/Python/Output/Edgar')
data_folder_out = Path('C:/Users/sscot/Dropbox (SRCMLLC)/SRCM/Python/Output/Edgar Out')


write_file = "FinFilingsProsp.txt"
file_to_write = data_folder_out / write_file


myFile = open(file_to_write, 'w')

linesIn = 0
linesOut= 0

print("reading files")
for y in range(1993, 2020):
    print('adding '+ str(y))
    for q in range(1,5):
        open_file = str(y) + '-QTR' + str(q) + '.tsv'
        file_to_open = data_folder / open_file
        inputs = []
        with open(file_to_open, 'r') as csv_file:
            for row in csv.reader(csv_file, delimiter='|'):
                inputs.append(row)
                linesIn = linesIn + 1
req_forms = ['F-1','S-1','S-1/A','F-1/A','424A','424B1','424B2','424B3','424B4','424B5','424B6','424B7','424B8']
print("filtering file")
output = [x for x in inputs if x[2] in req_forms]
print("writing file")
myFile = open(file_to_write, 'a', newline='')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(output)
    print(open_file)

print("writing index")      
index_write_file = "CIK_Name_IndexProsp.txt"
CIK_Name_to_write = data_folder_out / index_write_file
CIK_Name_Unique = {}

with open(file_to_write) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        key = row[0] + "-" + row[1]
        if key not in CIK_Name_Unique:
            CIK_Name_Unique.update({key : row})
            linesOut = linesOut + 1

print("Lines in " + str(linesIn))
print("Lines out " + str(linesOut))

sorted_x = sorted(CIK_Name_Unique.items(), key=operator.itemgetter(1))
sorted_dict = collections.OrderedDict(sorted_x)

(pd.DataFrame.from_dict(data=sorted_dict, orient='index')
   .to_csv(CIK_Name_to_write, header=False))


#      print(str(y)+"-QTR"+str(q))
#      print("Lines in " + str(len(inputs)))
#      print("Lines out " + str(len(output)))

# Version 1 using an array
#      output = [x for x in inputs if x[2] in req_forms]  # list

# version 2 using a dictionary
#with open(file_to_write) as csv_file:
#    csv_reader = csv.reader(csv_file, delimiter=',')
#    for row in csv_reader:
#        key = row[0] + "-" + row[1]
#        if key not in CIK_Name_Unique:
#            CIK_Name_Unique.update({key : row})
#            linesOut = linesOut + 1
# (pd.DataFrame.from_dict(data=CIK_Name_Unique, orient='index')
#   .to_csv(CIK_Name_to_write, header=False))

# Another version
#        output = {k : v for k, v in input.items() if v[1] in req_forms}
#        with open(file_to_write, 'w') as data:
#            data.write(str(output))
