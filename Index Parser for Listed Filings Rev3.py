from pathlib import Path
import csv
import pandas as pd
import operator
import collections
import pprint
import time
import os

# updated to have input files be in a new input directory
# added date and time one end of new files written
# need to add flag to write_records to include header or not
# for time being, just wrote new function

#need to change this code to just read in the big master list and then udate from teh last quarter availabe.  maybe the intersection of two sets would work.

# DA - Dropbox paths aren't consistent across users and operating systems
# SR - this doesn't work on a windows machine.  returns KeyError: 'C\\Users\sscot' on my machine.  I can't put that in as key either
DROPBOX_PATHS = {
    '/Users/david': '/Users/david/Dropbox/',
    'C:/Users/sscot': 'C:/Users/sscot/Dropbox (SRCMLLC)/SRCM/'
}
#dropbox_base_folder = Path(DROPBOX_PATHS[str(Path.home())])
#temp hack until I figure it out
dropbox_base_folder = Path('C:/Users/sscot/Dropbox (SRCMLLC)/SRCM/')

data_folder = dropbox_base_folder / 'Python/Input/Edgar Index Files'
data_folder_out = dropbox_base_folder / 'Python/Output/Edgar Out'

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

# DA - renamed to write_column since that's what you are doing, writing a list of single values (a column) rather than a list of rows
# DA - the reason you were getting values like "6,1,3,4,7" is because a single string looks like a sequence of chars so
# DA - writer.writerows is doing something like this:
# DA     for row in rows:
# DA        for field in row: # since row is just a string, iterating on it returns each individual character
# DA          write(field + ',')
# DA - below I'm just writing each record (string) to a separate line (note writelines doesn't add \n for some reason)
def write_column(input_file, records):
    def add_eol(lines):
        for item in lines:
            yield item + '\n'
    with open(input_file, 'w', newline='') as myFile:
        myFile.writelines(add_eol(records))

 # Load in all quarterly index files into a list named datarecords     

datarecords = []
start = time.process_time()
#add code in here so it does not break if you go out of range for the files
for y in range(1993, 2021):
    for q in range(1,5):
        open_file = str(y) + '-QTR' + str(q) + '.tsv'
        try:
            file_to_open = data_folder / open_file
            with open(file_to_open, 'r') as csv_file:
                # print("{}...{}".format(open_file, time.process_time() - start))
                datarecords.extend([_.strip().split('|') for _ in csv_file.readlines()])
        except:
            raise
            continue
print("{}...{}".format("Finished building Data Records Array", time.process_time() - start))
write_records(file_to_write("All_SEC_Filings_Index"), datarecords)
print("{}...{}".format("Finished Writing All_SEC_Filings_Index", time.process_time() - start))

FORM_TYPE_FLD = 2   # 3rd element contains the form type

# create dictionary where defult/new keys will be integers of 0
form_type_counts = collections.defaultdict(int)
form_cik_counts = collections.defaultdict(set)
for row in datarecords:
    form_type_counts[row[FORM_TYPE_FLD]] += 1
    form_cik_counts[row[FORM_TYPE_FLD]].add(row[0])

print("{}...{}".format("Writing Form_Type_CIK_Count", time.process_time() - start))
with open(file_to_write("Form_Type_CIK_Count"), 'w') as f:
    for key in sorted(form_type_counts.keys()):
        f.write("{:20}  {:5d}  {:5d}\n".format(key, form_type_counts[key], len(form_cik_counts[key])))

req_forms = ['10-K','10-Q','10-K/A','10-Q/A','10-QT', '10-KT','20-F','20-F/A', '6-F']
filtered_Filings = [row for row in datarecords if row[FORM_TYPE_FLD] in req_forms]

# THIS CODE DID NOT WORK  - PROGRAM IS NOW VERY VERY SLOW
#filtered_Filings= filtered_Filings.sort()

print("{}...{}".format("Writing Filtered_Qtr_Filers", time.process_time() - start))
write_records(file_to_write("Filtered_Qtr_Filers"), filtered_Filings)


CIK_Name_Unique = set()
for row in filtered_Filings:
    CIK_Name_Unique.add((row[0],row[1]))

# this doesn't work either - I want a unique list of CIK's
# this works now - it was just printing incorrectly but was creating a list which I tested by printing out
# THIS SEEMS VERY SLOW
# DA - don't waste time checking if row[0] is in CIK_Unique, just use a set like you had below. You thought it
# DA - was wrong because your routine to save to a file had an error
# CIK_Unique = []
# for row in filtered_Filings:
#     if row[0] not in CIK_Unique:
#         CIK_Unique.append(row[0])
# print(CIK_Unique)

# DA - uncommented this - it's MUCH faster than above
CIK_Unique = set()
for row in filtered_Filings:
    CIK_Unique.add(row[0])

print("{}...{}".format("Writing Filtered_CIK_Name", time.process_time() - start))   
write_records_no_header(file_to_write("Filtered_CIK_Name"), CIK_Name_Unique)

# this does not work when I print to file - puts commas between the characters in the string
# corrected it by new function with []
# DA - see changes to write_column above. Works now
print("{}...{}".format("Writing Filtered_CIK", time.process_time() - start))   
write_column(file_to_write("CIK_Unique"), CIK_Unique)

# this now works.
print("{}...{}".format("Retrieving filings for quarterly filings", time.process_time() - start))   
# DA - this is where most of the script spends its time
all_filtered_Filings = [row for row in datarecords if row[0] in CIK_Unique]
write_records_no_header(file_to_write("All_Filtered_Qtr_Filer"), all_filtered_Filings)
print("{}...{}".format("FINSIHED", time.process_time() - start))   