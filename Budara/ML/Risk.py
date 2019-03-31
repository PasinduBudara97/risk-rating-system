import pandas as pd
import numpy as np
from IPython.display import display
import matplotlib.pyplot as plt

data = pd.read_csv("credit_train.csv")
display(data.head(n=5))
data.isnull().any()
n_crib=data.shape[0]


crib_is_null=data.loc[(data['crib']==None)]
n_null=crib_is_null.shape[0]

crib_greater_60=data.loc[(data['crib']>60)]
n_greater_than_60=crib_greater_60.shape[0]

crib_btwn_30and60=data.loc[(data['crib'] <60) & (data['crib'] >30)]
n_btwn_30and60=crib_btwn_30and60.shape[0]

crib_less_30=data.loc[(data['crib']<30)]
n_less_30=crib_less_30.shape[0]

crib_is_zero=data.loc[(data['crib']==0)]
n_zero=crib_is_zero.shape[0]

good_crib=n_zero*100/n_crib

print("Total no of loan data: []".format(n_crib))
print("Loan with no crib history: []".format(n_null))
print("Loan with crib greater than 60: []".format(n_greater_than_60))
print("Loan with crib between 30and60: []".format(n_btwn_30and60))
print("Loan with crib less than 30: []".format(n_less_30))
print("Loan with crib equals to 0: []".format(n_zero))