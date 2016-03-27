import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import statsmodels.api as sm


#open loan data
df = pd.read_csv('LoanStats.csv', header=1, low_memory=False)
df.dropna(inplace=False)


#format issue_d to datetime format and set it as the index
df['issue_d_format'] = pd.to_datetime(df['issue_d'], format='%b-%y')
print(df['issue_d_format'].head())
dfts = df.set_index('issue_d_format')


#converting and grouping 
year_month_summary = dfts.groupby(lambda x : x.year * 100 + x.month).count()


loan_count_summary = year_month_summary['issue_d']

#plotting loan count
loan_count_summary.plot()
plt.show()

#plot auto regression
sm.graphics.tsa.plot_acf(loan_count_summary)
plt.show()


#plot partial auto regression
sm.graphics.tsa.plot_pacf(loan_count_summary)
plt.show()