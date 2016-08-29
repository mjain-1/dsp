# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

football = pd.read_csv('https://raw.githubusercontent.com/mjain-1/dsp/master/python/football.csv')

football["Difference"] = football["Goals"] - football["Goals Allowed"]

## Assuming smallest positive difference 
football = football[football["Difference"]>0]

## Returns team with smallest difference
print ("Team with smallest difference: ", football[football["Difference"] == football["Difference"].min()]["Team"].to_string(index = False))
