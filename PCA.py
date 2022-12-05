import pandas
import numpy
import seaborn
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

file_name = 'data.xlsx'
data_file = pandas.read_excel(file_name)
data_file.drop('№', inplace=True, axis=1)
data_file.drop('Область', inplace=True, axis=1)
df_normalized=(data_file - data_file.mean()) / data_file.std()
pca = PCA(n_components=data_file.shape[1])
pca.fit(df_normalized)

# Reformat and view results
loadings = pandas.DataFrame(pca.components_.T,
columns=['PC%s' % _ for _ in range(len(df_normalized.columns))],
index=data_file.columns)
plt.plot(pca.explained_variance_ratio_)
plt.ylabel('Explained Variance')
plt.xlabel('Components')
plt.show()
