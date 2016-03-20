import pandas as pd
import numpy as np
import statsmodels.api as sm


df = pd.read_csv('loansData_clean_full.csv')

x1 = df['Annual.Income']
y1 = df['Interest.Rate']

X1 = sm.add_constant(x1)

inc_int_model = sm.OLS(y1, X1).fit()

print(inc_int_model.summary())


x2 = df[['Annual.Income', 'Home.Owner']]
y2 = df['Interest.Rate']

X2 = sm.add_constant(x2)

inc_int_own_model = sm.OLS(y2, X2).fit()

print(inc_int_own_model.summary())

