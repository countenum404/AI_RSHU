import pandas
import numpy
import seaborn
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import KMeans


file_name = 'data.xlsx'
data_file = pandas.read_excel(file_name, usecols=['Область', 'ПТиОУ', 'ОПив', 'ПН', 'ПФА', 'ДР'])
data = []
for i in range(data_file.shape[0]):
    data.append(list(data_file.iloc[i])[1:])

model = KMeans(n_clusters=4)
model.fit(data)
data_file['clusters'] = model.labels_
print(data_file)