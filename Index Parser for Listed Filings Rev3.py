from pathlib import Path
import csv
import pandas as pd
import operator
import collections
import pprint
import time

data_folder = Path('C:/Users/sscot/Dropbox (SRCMLLC)/SRCM/Python/Output/Edgar')
data_folder_out = Path('C:/Users/sscot/Dropbox (SRCMLLC)/SRCM/Python/Output/Edgar Out')


write_file = "FinFilings.txt"
file_to_write = data_folder_out / write_file

def write_records(file_to_write, records):
    with open(file_to_write, 'w', newline='') as myFile:
        writer = csv.writer(myFile)
        writer.writerow(['cik', 'name', 'form_type', 'filing_date', 'form_text_url', 'form_html_url'])
        writer.writerows(records)
       

datarecords = []
start = time.clock()
for y in range(1993, 2020):
    for q in range(1,5):
        open_file = str(y) + '-QTR' + str(q) + '.tsv'
        file_to_open = data_folder / open_file
        with open(file_to_open, 'r') as csv_file:
            print("{}...{}".format(open_file, time.clock() - start))
            #reader = csv.reader(csv_file, delimiter='|')
            #inputs.extend(list(reader))
            datarecords.extend([_.strip().split('|') for _ in csv_file.readlines()])
            #for row in csv.reader(csv_file, delimiter='|'):
            #    inputs.append(row)
            #    linesIn = linesIn + 1

FORM_TYPE_FLD = 2

# create dictionary where defult/new keys will be integers of 0
form_type_counts = collections.defaultdict(int)
form_cik_counts = collections.defaultdict(set)
for row in datarecords:
    form_type_counts[row[FORM_TYPE_FLD]] += 1
    form_cik_counts[row[FORM_TYPE_FLD]].add(row[0])

print("Form Type/CIK Counts")
with open(data_folder_out / "Form Type and CIK Counts.txt", 'w') as f:
    for key in sorted(form_type_counts.keys()):
        f.write("{:20}  {:5d}  {:5d}\n".format(key, form_type_counts[key], len(form_cik_counts[key])))

req_forms = ['10-K','10-Q','10-K/A','10-Q/A','10-QT', '10-KT','20-F','20-F/A', '6-F']
output = [row for row in datarecords if row[FORM_TYPE_FLD] in req_forms]

write_records(data_folder_out / "AllFinFilings.txt", datarecords)
write_records(file_to_write, output)


index_write_file = "CIK_Name_Index.txt"
CIK_Name_to_write = data_folder_out / index_write_file
CIK_Name_Unique = {}

with open(file_to_write) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        key = row[0] + "-" + row[1]
        if key not in CIK_Name_Unique:
            CIK_Name_Unique.update({key : row})

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
