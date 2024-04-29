

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Loading dataset
data = pd.read_csv('/content/drive/MyDrive/Datasets/1_least_squared_method_salary.csv')
data.head()

# Plotting the data
plt.figure(figsize = (5, 5))
plt.scatter(data['exp'],data['salary'])

# Computing X and Y
X = data['exp'].values
Y = data['salary'].values

mean_x = np.mean(X)
mean_y = np.mean(Y)

n = len(X)

print('mean_x= ',mean_x,'mean_y= ', mean_y, 'n= ',n)

num = 0
denom = 0
for i in range(n):
  num += (X[i] - mean_x) * (Y[i] - mean_y)
  denom += (X[i] - mean_x) ** 2
  m = num / denom
  c = mean_y - (m * mean_x)

print("Coefficients")
print('m= ',m, 'c= ', c)

maxx_x = np.max(X) + 10
minn_x = np.min(X) - 10

x = np.linspace(minn_x, maxx_x, 1000)
y = c + m * x

plt.figure(figsize = (5, 5))
plt.plot(x, y, color='#58b970', label='Regression Line')
plt.scatter(X, Y, c='#ef5423', label='Scatter Plot')
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.legend()
plt.show()

