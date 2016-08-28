import pandas as pd
import re

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
 
def extract_pos(pos):
    pos = str(pos)
    found = []
    if len(re.findall('Assist', pos)) >= 1:
        found.append('Assistant Professor')
    if len(re.findall('Associate', pos)) >= 1:
        found.append('Associate Professor')
    if len(re.findall('^Professor', pos)) >= 1:
        found.append('Professor')
    return found
    
def extract_domain(email):
    email = str(email)
    return re.findall('(?<=@)[a-z.]*', email)[0]
    
faculty = pd.read_csv('/Users/meghajain/Desktop/faculty.csv')

all_deg = dict()
    
for deg in faculty[' degree']:
    indiv_deg = extract_deg(deg)
    for degree in indiv_deg:
        if degree not in all_deg:
            all_deg[degree] = 1
        else:
            all_deg[degree] += 1

all_pos = dict()
for pos in faculty[' title']:
    indiv_pos = extract_pos(pos)
    for position in indiv_pos:
        if position not in all_pos:
            all_pos[position] = 1
        else:
            all_pos[position] += 1

emails = []
domains = []
for email in faculty[' email']:
    emails.append(email)
    domain = extract_domain(email)
    if domain not in domains:
        domains.append(domain)

print("Degrees and their frequencies: ", all_deg)
print("Positions and their frequencies: ", all_pos)     
print("Emails: ", emails)
print("Unique domains: ", domains)   
