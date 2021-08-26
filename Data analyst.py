# %% - import libraries
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
# %% - prepare data
#reshape(-1,1) de bien data thanh dang cot
income = np.array([8,9,10,11,12,15,15,16,17,18,18,20,24,25,25]).reshape(-1,1)
expenditure = np.array([6,7,9,9,10,12,11,13,13,15,14,16,18,20,19])
# %% - create model

model = LinearRegression().fit(income,expenditure)
R_sq= model.score(income,expenditure)

intercept=model.intercept_
slope=model.coef_

plt.scatter(income,expenditure)
plt.xlabel(income)
plt.ylabel(expenditure)
plt.plot(income,intercept + slope*income)
plt.show()
# %% - predict response
income_new= np.array([26,28]).reshape(-1,1)
pre_value = model.predict(income_new)