import matplotlib.pyplot as plt
import numpy as numpy
import scipy.stats as stats

data = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

plt.figure
plt.boxplot(data)
plt.savefig('boxandwhisker.png')
plt.close()

plt.figure
plt.hist(data, histtype='bar')
plt.savefig('hist.png')
plt.close()

plt.figure
graph1 = stats.probplot(data, dist="norm", plot=plt)
plt.savefig('qq.png')
plt.close()