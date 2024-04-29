

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
data=pd.read_csv('/content/drive/MyDrive/Datasets/4_KNN_datapoints.csv')
data.head()

import matplotlib.pyplot as plt
plt.figure(figsize = (4, 4))
plt.scatter(data['VAR1'],data['VAR2'])
plt.xlabel('VAR1')
plt.ylabel('VAR2')
plt.show()

x=pd.DataFrame(data[['VAR1','VAR2']])
x[:5]

from sklearn.cluster import KMeans
km=KMeans(3)
km.fit(x)

clusters=km.fit_predict(x)
clusters

data_with_output=data.copy()
data_with_output[:5]

data_with_output['Cluster']=clusters
data_with_output

plt.figure(figsize = (4, 4))
plt.scatter(data_with_output['VAR1'], data_with_output['VAR2'],c=data_with_output['Cluster'], cmap='rainbow' )

datanew=[[0.906,0.606],[1.23,0.98],[0.234,0.432]]
df1=pd.DataFrame(datanew,columns=['NewVar1','NewVar2'])
df1

cnew=km.fit_predict(df1)
cnew
