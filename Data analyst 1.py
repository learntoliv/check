# %% - import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
# %% - prepare data
df = pd.read_csv('../Data/Income.csv')
income = df['income']
expenditure = df['expenditure']
income = np.array(income)
expenditure = np.array(expenditure)
income = sm.add_constant(income)
# %% - create model

model = sm.OLS(expenditure,income)
results = model.fit()

# %% - Get results

R_sq = results.rsquared
hs = results.params
print(results.summary())

plt.scatter(df['income'],df['expenditure'])
plt.plot(df['income'], hs[0] + hs[1]*df['income'])
plt.show()
# %% - predict response
income_new = np.array([26,28,30])
income_new = sm.add_constant(income_new)
results.predict(income_new)

