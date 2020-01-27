from pathlib import Path
import csv
import pandas as pd
import operator
import collections
import pprint
import time

# updated to have input files be in a new input directory
# added date and time one end of new files written
# need to add flag to write_records to include header or not
# for time being, just wrote new function

data_folder = Path('C:/Users/sscot/Dropbox (SRCMLLC)/SRCM/Python/Input/Edgar Index Files')
data_folder_out = Path('C:/Users/sscot/Dropbox (SRCMLLC)/SRCM/Python/Output/Edgar Out')

def file_to_write(file_name):
    timestr = time.strftime("%Y-%m-%d-%H-%M")
    full_file_name = file_name + " " + timestr + ".txt"
    file_and_path = data_folder_out / full_file_name
    return(str(file_and_path))

def write_records(input_file, records):
    with open(input_file, 'w', newline='') as myFile:
        writer = csv.writer(myFile)
        writer.writerow(['cik', 'name', 'form_type', 'filing_date', 'form_text_url', 'form_html_url'])
        writer.writerows(records)

def write_records_no_header(input_file, records):
    with open(input_file, 'w', newline='') as myFile:
        writer = csv.writer(myFile)
        writer.writerows(records)

 # Load in all quarterly index files into a list named datarecords     

datarecords = []
#start = time.clock()
for y in range(1993, 1995):
    for q in range(1,5):
        open_file = str(y) + '-QTR' + str(q) + '.tsv'
        file_to_open = data_folder / open_file
        with open(file_to_open, 'r') as csv_file:
#            print("{}...{}".format(open_file, time.clock() - start))
            datarecords.extend([_.strip().split('|') for _ in csv_file.readlines()])

write_records(file_to_write("All_SEC_Filings_Index"), datarecords)

       
FORM_TYPE_FLD = 2   # 3rd element contains the form type

# create dictionary where defult/new keys will be integers of 0
form_type_counts = collections.defaultdict(int)
form_cik_counts = collections.defaultdict(set)
for row in datarecords:
    form_type_counts[row[FORM_TYPE_FLD]] += 1
    form_cik_counts[row[FORM_TYPE_FLD]].add(row[0])

with open(file_to_write("Form_Type_CIK_Count"), 'w') as f:
    for key in sorted(form_type_counts.keys()):
        f.write("{:20}  {:5d}  {:5d}\n".format(key, form_type_counts[key], len(form_cik_counts[key])))

req_forms = ['10-K','10-Q','10-K/A','10-Q/A','10-QT', '10-KT','20-F','20-F/A', '6-F']
filtered_Filings = [row for row in datarecords if row[FORM_TYPE_FLD] in req_forms]
write_records(file_to_write("Filtered_Qtr_Filers"), filtered_Filings)


CIK_Name_Unique = set()
for row in filtered_Filings:
    CIK_Name_Unique.add((row[0],row[1]))
write_records_no_header(file_to_write("Filtered_CIK_Name"), CIK_Name_Unique)