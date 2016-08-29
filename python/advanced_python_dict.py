import pandas as pd
import re
import csv
from collections import OrderedDict

def extract_deg(deg):
    deg = str(deg)
    found = []
    if len(re.findall('Ph[.]*D', deg)) >= 1:
        found.append('Ph.D.')
    if len(re.findall('B[.]*S[.]*Ed[.]', deg)) >= 1:
        found.append('B.S.Ed.')
    if len(re.findall('M[.]*S[.]*', deg)) >= 1:
        found.append('M.S.')
    if len(re.findall('JD', deg)) >= 1:
        found.append('J.D.')
    if len(re.findall('MPH', deg)) >= 1:
        found.append('M.P.H.')
    if len(re.findall('MA', deg)) >= 1:
        found.append('M.A.')
    if len(re.findall('Sc[.]*D', deg)) >= 1:
        found.append('Sc.D.')
    return " ".join(found)

def extract_pos(pos):
    pos = str(pos)
    if len(re.findall('Assist', pos)) >= 1:
        return 'Assistant Professor'
    if len(re.findall('Associate', pos)) >= 1:
        return 'Associate Professor'
    if len(re.findall('^Professor', pos)) >= 1:
        return 'Professor'
    
def first_name(name):
    name = str(name)
    names = name.split(" ")
    return names[0]
    
def last_name(name):
    name = str(name)
    names = name.split(" ")
    if len(names) > 2:
        return names[2]
    else:
        return names[1]
        
    
faculty = pd.read_csv('/Users/meghajain/Desktop/faculty.csv') 

##Splits name into first and last; standardizes degree and title.
faculty['first_name'] = faculty['name'].map(first_name)
faculty['last_name'] = faculty['name'].map(last_name)
faculty[' degree'] = faculty[' degree'].map(extract_deg)
faculty[' title'] = faculty[' title'].map(extract_pos)

faculty.drop('name', inplace = True, axis = 1)

faculty.to_csv('/Users/meghajain/Desktop/faculty1.csv')

rows = []
with open('/Users/meghajain/Desktop/faculty1.csv', 'r') as f:
    reader = csv.reader(f, dialect = 'excel')
    for row in reader:
        rows.append(row)
     
##Creates dictionary with key as last name 
faculty_dict = {}
for row in rows:
    k, v = row[5], row[1:4]
    if k not in faculty_dict:
        faculty_dict[k] = [v]
    else:
        faculty_dict[k].append(v)
    

##Creates dictionary with key as first, last sorted by first 
professor_dict = {}
for row in rows:
    k, v = (row[4], row[5]), row[1:4]
    if k not in faculty_dict:
        professor_dict[k] = v
    else:
        professor_dict[k].append(v)
        
    
##Creates dictionary with key as first, last sorted by last    
professor_last_dict = (OrderedDict(sorted(professor_dict.items(), key = lambda x: x[0][1])))
