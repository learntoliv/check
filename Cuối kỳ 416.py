# %% - import libraries
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression as lr
import numpy as np
import statsmodels.api as sm
# %% - prepare data

df= pd.read_csv('../Data/Sales-Ck416.csv')
week = np.array(df['Week'])
sales_volume = np.array(df['Sales_Volume'])
price = np.array(df['Price'])
price_sm = sm.add_constant(np.array(df['Price']))
ads_cost = np.array(df['Ads_Cost'])
ads_cost_sm = sm.add_constant(np.array(df['Ads_Cost']))

# %% - create model

model_price = sm.OLS(price,sales_volume).fit()
model_adscost = sm.OLS(ads_cost,sales_volume).fit()
hs1 = model_price.params
hs2 = model_adscost.params

plt.scatter(df['Price'],df['Sales_Volume'])
#plt.scatter(df['Ads_Cost'],df['Sales_Volume'])
plt.show()
# %% - predict response
