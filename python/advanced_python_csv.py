import pandas as pd
import csv

faculty = pd.read_csv('/Users/meghajain/Desktop/faculty.csv')   

## Two ways to create csv file of emails: 

## Use pandas, though this will create a column with the index for each row
faculty[' email'].to_csv("/Users/meghajain/emails.csv") 

## Use csv module, this is the file I uploaded to repository.

emails = [[email] for email in faculty[' email']]

with open('/Users/meghajain/Desktop/emails.csv', 'w') as f:
    writer = csv.writer(f, dialect = 'excel')
    writer.writerows(emails)
