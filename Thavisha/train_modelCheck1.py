import pandas as pd
from random import shuffle
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
import time
import pickle


cols=['Loan no','Ammount','Period','EMI','purpose','secutityType','CRIB','entity','POS','assets','installments','tax']
df=pd.read_excel('/home/Desktop/failed_data.xlsx',index_col=0)

ammount=df['Loan amount']
period=df['Period']
emi=df['EMI']                                    
POL=df['Purpose of loan']
newPOL=[]
security=df['Security type']
newSecurity=[]
CRIB=df['CRIB status']
newCRIB=[]
TOE=df['type of entity']
newTOE=[]
POS=df['period of service(yrs)']
assets=df['Total assets']
loanI=df['loan installments']
tax=df['tax paying']
newTax=[]


def setPOL(POL):
    for i in range(len(POL)):
        sample=POL[i+1]
        if(sample=="Purchase of Machinery & Equipment"):
            newPOL.append(0)
        elif(sample=="Purchase") or (sample=="Purchase ") :
            newPOL.append(1)
        elif(sample=="Business & Redemption"):
            newPOL.append(2)
        elif(sample=="Education"):
            newPOL.append(3)
        elif(sample=="Renovation/Repair(Improvement)"):
            newPOL.append(4)
        elif(sample=="Redemption"):
            newPOL.append(5)
        elif(sample=="Business"):
            newPOL.append(6)
        elif(sample=="Purchase Of House"):
            newPOL.append(7)
        elif(sample=="OTHER"):
            newPOL.append(8)
        elif(sample=="Transport & Storage"):
            newPOL.append(9)
        elif(sample=="Redemption & Construction"):
            newPOL.append(10)
        elif(sample=="Construction"):
            newPOL.append(11)
        elif(sample=="Purchasing Of Building Block"):
            newPOL.append(12)
        elif(sample=="Business Use only"):
            newPOL.append(13)
        elif(sample=="Expansion of Business"):
            newPOL.append(14)
        elif(sample=="Agriculture/Farming"):
            newPOL.append(15)
        elif(sample=="Furnitures"):
            newPOL.append(16)
        elif(sample=="Redemption & Furniture"):
            newPOL.append(17)
        elif(sample=="Dairy and Poultry Products"):
            newPOL.append(18)