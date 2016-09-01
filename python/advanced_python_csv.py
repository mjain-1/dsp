import pandas as pd
import csv

faculty = pd.read_csv('/Users/meghajain/Desktop/faculty.csv')   

## Two ways to create csv file of emails: 

## Use pandas.
faculty[' email'].to_csv("/Users/meghajain/emails.csv", index = False) 

## Use csv module.

emails = [[email] for email in faculty[' email']]

with open('/Users/meghajain/Desktop/emails.csv', 'w') as f:
    writer = csv.writer(f, dialect = 'excel')
    writer.writerows(emails)
