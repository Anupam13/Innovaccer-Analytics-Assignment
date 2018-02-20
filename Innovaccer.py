import pandas as pd
x = pd.read_csv('problem.csv')
last = x.ln.str.split('\s+').str[0]
first=  x.fn.str.split('\s+').str[0]
name = first + ' ' + last
x.insert(0,"Name",name)
data = x[['Name','dob','gn']]
final = data.drop_duplicates()
final.index = range(len(final))
final.index = final.index + 1
final.to_csv('Output.csv')