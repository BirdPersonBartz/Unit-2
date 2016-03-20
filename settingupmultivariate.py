import pandas as pd
import numpy as np

df = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')
df.dropna(inplace=True)

df['Interest.Rate'] = [float(interest[0:-1])/100 for interest in df['Interest.Rate']]
df['Annual.Income'] = [float(val * 12) for val in df['Monthly.Income']]
df['Home.Owner'] = np.where((df['Home.Ownership'] == 'OWN') | (df['Home.Ownership'] == 'MORTGAGE'), 1, 0)


df.to_csv('loansData_clean_full.csv', header=True, index=False)

