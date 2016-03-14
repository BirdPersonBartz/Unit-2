import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

#open data and put into pd dataframe
loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')
loansData.dropna(inplace=True)

#build boxplots for both columns
loansData.boxplot(column = 'Amount.Requested')
plt.savefig('ARbox.png')
loansData.boxplot(column = 'Amount.Funded.By.Investors')
plt.savefig('AFbox.png')


#build histograms for both columns
loansData.hist(column = 'Amount.Requested')
plt.savefig('ARhist.png')
loansData.hist(column = 'Amount.Funded.By.Investors')
plt.savefig('AFhist.png')



#bulid qq's for both columns, saving in all using savefig()
plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist='norm', plot = plt)
plt.savefig('AFQQ.png')
plt.figure()
graph = stats.probplot(loansData['Amount.Funded.By.Investors'], dist='norm', plot = plt)
plt.savefig('AFQQ.png')