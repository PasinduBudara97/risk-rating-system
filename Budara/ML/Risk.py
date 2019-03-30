import pandas as pd
import numpy as np
from IPython.display import display
import matplotlib.pyplot as plt

data = pd.read_csv("credit_train.csv")
display(data.head(n=5))
data.isnull().any()