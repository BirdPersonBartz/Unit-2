from scipy import stats

import matplotlib.pyplot as plt
import collections
import pandas as pd

loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')
loansData.dropna(inplace=True)

plt.figure()
chip= stats.chisquare(loansData['Open.CREDIT.Lines'])



plt.show()




#plt.figure()
#plt.bar(freq.keys(), freq.values(), width = 1)
#plt.show()


