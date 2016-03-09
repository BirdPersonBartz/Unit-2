import pandas as pd
import scipy 
import scipy.stats as stats
#stats has to imported by itself from scipy
data = '''Region,Alcohol,Tobacco
			North,6.47,4.03
			Yorkshire,6.13,3.76
			Northeast,6.19,3.77
			East Midlands,4.89,3.34
			West Midlands,5.63,3.47
			East Anglia,4.52,2.92
			Southeast,5.89,3.20
			Southwest,4.79,2.71
			Wales,5.27,3.53
			Scotland,6.08,4.51
			Northern Ireland,4.02,4.56'''

#this takes the data, splits it on lines, then commas, and /n signals new line
data = data.splitlines()
data = [i.split(',') for i in data]


#assigns column_names to the row with the headers
column_names = data[0]

#assigns data_rows to the remeaing rows of data
data_rows = data[1::]

#builds the PD data frame from the assignments above
df = pd.DataFrame(data_rows, columns=column_names)

#float the numbers
df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

print("The mean for the Alcohol and Tobacco dataset is %s for Alcohol and %s for Tobacco" % (round(df['Alcohol'].mean(),3), round(df['Tobacco'].mean(),3)))
print("The median for the Alcohol and Tobacco dataset is %s for Alcohol and %s for Tobacco" % (df['Alcohol'].median(), df['Tobacco'].median()))
print("The mode for the Alcohol and Tobacco dataset is %s for Alcohol and %s for Tobacco" % (stats.mode(df['Alcohol']), stats.mode(df['Tobacco']))
print("The range for the Alcohol and Tobacco dataset is %s for Alcohol and %s for Tobacco" % (max(df['Alcohol'])-min(df['Alcohol']), max(df['Tobacco'])-min(df['Tobacco']))
print("The variance for the Alcohol and Tobacco dataset is %s for Alcohol and %s for Tobacco" % (round(df['Alcohol'].var(),3), round(df['Tobacco'].var(),3)))
print("The standard deviation for the Alcohol and Tobacco dataset is %s for Alcohol and %s for Tobacco" % (round(df['Alcohol'].std(),3), round(df['Tobacco'].std(),3)))
