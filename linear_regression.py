import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
import statsmodels.api as sm


loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

#remove % symbol convert to float. Using lists comp. Made a lot more sense to me than Lamda expressions
#although lambda would look like cleanInterestRate = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))
loansData['Interest.Rate'] = [float(interest[0:-1])/100 for interest in loansData['Interest.Rate']]

#remove "month" and convert to integer
loansData['Loan.Length'] = [int(length[0:-7]) for length in loansData['Loan.Length']]

#create a new column Fico Score with lower value
loansData['FICO.Score'] = [int(val.split('-')[0]) for val in loansData['FICO.Range']]



#creating variables out of the columns
intrate = loansData['Interest.Rate']
laonamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']


#placing into the matrix
y = np.matrix(intrate).transpose()
x1 = np.matrix(fico).transpose()
x2 = np.matrix(laonamt).transpose()

#stacking the values of x1 next to x2
x = np.column_stack([x1,x2])

X = sm.add_constant(x)
model = sm.OLS(y,X)


print(f.summary())