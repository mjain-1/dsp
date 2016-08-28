import pandas as pd
import re

## Ex 1
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
    return found
 
faculty = pd.read_csv('/Users/meghajain/Desktop/faculty.csv')

all_deg = dict()
    
for deg in faculty[" degree"]:
    indiv_deg = extract_deg(deg)
    for degree in indiv_deg:
        if degree not in all_deg:
            all_deg[degree] = 1
        else:
            all_deg[degree] += 1
            
print("Degrees and their frequency: " all_deg)
