import pickle
import pandas as pd
import numpy as np

modelfile = '../TrainedModel/finalizedModel.sav'
datafile = '../Textfiles/testBank.csv'
savedfile = "../Textfiles/prediction.txt"
loaded_model = pickle.load(open(modelfile, 'rb'), encoding='latin1')
cols = ['Ammount', 'Period', 'EMI', 'purpose', 'secutityType', 'CRIB', 'entity', 'POS', 'assets', 'installments', 'tax']
df = pd.read_csv(datafile, sep=",", header=None, names=cols)

ammount = df['Ammount']
period = df['Period']
emi = df['EMI']
POL = df['purpose']
newPOL = None
security = df['secutityType']
newSecurity = None
CRIB = df['CRIB']
newCRIB = None
TOE = df['entity']
newTOE = None
POS = df['POS']
assets = df['assets']
loanI = df['installments']
tax = df['tax']
newTax = None


def PreProcessData(getData):
    sum = 0
    for i in range(len(getData)):
        sum = sum + getData[i]
    tList = (
    ammount[0] / sum, period[0] / sum, emi[0] / sum, newPOL / sum, newSecurity / sum, newCRIB / sum, newTOE / sum,
    POS[0] / sum, assets[0] / sum, loanI[0] / sum, newTax / sum)
    return tList