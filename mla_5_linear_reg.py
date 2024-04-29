

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

data=pd.read_csv('/content/sat_gpa (1).csv')

data[:5]

data['SAT'][:5]

y=data['GPA'] # Dependent Variable
x1=data['SAT'] # Independent Variable

plt.figure(figsize = (4, 4))
plt.scatter(x1,y)
plt.xlabel('SAT Data')
plt.ylabel('GPA Data')
plt.show()

x=sm.add_constant(x1)

results=sm.OLS(y,x).fit()

results.summary()

plt.figure(figsize = (4, 4))
plt.scatter(x1,y)
yhat=0.0017 * x1 + 0.2750 # Regression Equation
plt.plot(x1,yhat) # Plotting the Regression Line
plt.xlabel('SAT')
plt.ylabel('GPA')

GPA= 0.2750 + 0.0017 * 1700
GPA
