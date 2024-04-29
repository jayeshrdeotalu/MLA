

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = pd.read_csv('/content/countries (1).csv')
data[:3]

plt.figure(figsize = (4, 3))
plt.scatter(dataframe["Latitude"], dataframe["Longitude"])
plt.xlabel("Latitude")
plt.ylabel("Longitude")

x=pd.DataFrame(data[['Latitude','Longitude']])
x[:3]

km=KMeans(3)
km.fit(x)

clusters=km.fit_predict(x)
clusters

data_with_output=data.copy()
data_with_output[:3]

data_with_output['Cluster']=clusters
data_with_output[:3]

plt.figure(figsize = (4, 3))
plt.scatter(data_with_output['Latitude'], data_with_output['Longitude'],c=data_with_output['Cluster'], cmap='rainbow')

