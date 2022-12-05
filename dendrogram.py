import pandas
import numpy
import seaborn
import matplotlib.pyplot
import scipy.cluster.hierarchy
from scipy.cluster.hierarchy import dendrogram, linkage


file_name = 'data.xlsx'
data_file = pandas.read_excel(file_name, usecols=['Область', 'ПТиОУ', 'ОПив', 'ПН', 'ПФА', 'ДР'])
print(data_file)
data = []
for i in range(data_file.shape[0]):
    data.append(list(data_file.iloc[i])[1:])
print(data)
dendrogram = dendrogram(linkage(data, method='ward'))
matplotlib.pyplot.title('v10')
matplotlib.pyplot.show()