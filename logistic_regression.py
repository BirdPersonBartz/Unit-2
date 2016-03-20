import pandas as pd
import numpy as np 
import statsmodels.api as sm

#taking user input
userfico = int(input('Enter your FICO score: '))
useramount = int(input('Enter the amount of your requested loan: '))

#reading cleaned loan data
df = pd.read_csv('loansData_clean.csv')

#making a new column of boonleans with True if int rate is > 12%
df['IR_TF'] = np.where(df['Interest.Rate'] > .12,1,0)

#print(loansDatadf['Interest.Rate'].head())
#print(loansDatadf['IR_TF'].head())


#making intercept column
df['intercept'] = 1.0



ind_vars = ['FICO.Score', 'Amount.Requested', 'intercept']

#interest_rate = b + a1(750) + a2(10000)


#running logistic regression to get testable coefficients
logit = sm.Logit(df['IR_TF'], df[ind_vars])
result = logit.fit()
coeff = result.params


#pluggin user values into expression to get p
	p = 1/(1 + 2.71828182846**(coeff[2]+ coeff[1]*Amount + coeff[0]*FICO))
	pred(p)


#taking p and printing if the loan will be funded with 12% or above
def pred(p):
	if p > 0.7:
		print("loan will be approved with 12 percent interest")
	else:
		print("loan will not be approved")





logistic_regression(userfico, useramount)