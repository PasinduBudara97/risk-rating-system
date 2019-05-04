import pickle
import pandas as pd
import numpy as np

modelfile = '/home/sadesh manranju/Desktop/finalizedModel.sav'
datafile='/home/sadesh manranju/Desktop/testBank.csv'
savedfile="/home/sadesh manranju/Desktop/prediction.txt"

loaded_model = pickle.load(open(modelfile , 'rb'))
cols=['Ammount','Period','EMI','purpose','secutityType','CRIB','entity','POS','assets','installments','tax']
df = pd.read_csv(datafile, sep=",", header=None, names=cols)


ammount=df['Ammount']
period=df['Period']
emi=df['EMI']                                    
POL=df['purpose']
newPOL=None
security=df['secutityType']
newSecurity=None
CRIB=df['CRIB']
newCRIB=None
TOE=df['entity']
newTOE=None
POS=df['POS']
assets=df['assets']
loanI=df['installments']
tax=df['tax']
newTax=None
