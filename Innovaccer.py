#import pandas library
import pandas as pd
x = pd.read_csv('input.csv')
#Separating strings for first and last name, and then taking the first part of each string .
last = x.ln.str.split('\s+').str[0]
first=  x.fn.str.split('\s+').str[0]
#creating a column 'name' and adding it to dataframe.
name = first + ' ' + last
x.insert(0,"Name",name)
#new dataframe with the 3 important variables as columns.
data = x[['Name','dob','gn']]
#using drop_duplicates() function to get unique patients fot the given dataset.
final = data.drop_duplicates()
final.index = range(len(final))
final.index = final.index + 1
# Output.csv created
final.to_csv('Output.csv')
