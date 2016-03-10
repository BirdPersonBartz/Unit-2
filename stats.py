import pandas as pd
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



#get the mode in the numpy array
modeT = stats.mode(df['Tobacco'])
modeA = stats.mode(df['Alcohol'])
#convert to string for portion I need
modeA = str(modeA[0:15])
modeT = str(modeT[0:15])

#Get the mean, roud to 3 deicmals
means = "The mean for the Alcohol and Tobacco dataset is %s for Alcohol and %s for Tobacco. " % (round(df['Alcohol'].mean(),3), round(df['Tobacco'].mean(),3))
#get median
medians = "The median for the Alcohol and Tobacco dataset is %s for Alcohol and %s for Tobacco. " % (df['Alcohol'].median(), df['Tobacco'].median())
#pick out the digits here. Bad code but what syntax could I use to make this better??
modes = "The mode for the Alcohol and Tobacco dataset is %s for Alcohol and %s for Tobacco. " % (modeA[9:13], modeT[9:13])
#get var and round
var = "The variance for the Alcohol and Tobacco dataset is %s for Alcohol and %s for Tobacco. " % (round(df['Alcohol'].var(),3), round(df['Tobacco'].var(),3))
#get stan d and round
stanD = ("The standard deviation for the Alcohol and Tobacco dataset is %s for Alcohol and %s for Tobacco." % (round(df['Alcohol'].std(),3), round(df['Tobacco'].std(),3)))


#print everything
print(means, medians, modes, var, stanD)

