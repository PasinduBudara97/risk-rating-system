import pickle
import pandas as pd
import numpy as np

modelfile = '/home/sahanakaw/Desktop/finalizedModel.sav'
datafile='/home/sahanakaw/Desktop/testBank.csv'
savedfile="/home/sahanakaw/Desktop/prediction.txt"

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

sample=POL[0]
if(sample=="Purchase of Machinery & Equipment"):
    newPOL=0
elif(sample=="Purchase") or (sample=="Purchase ") :
    newPOL=1
elif(sample=="Business & Redemption"):
    newPOL=2
elif(sample=="Education"):
    newPOL=3
elif(sample=="Renovation/Repair(Improvement)"):
    newPOL=4
elif(sample=="Redemption"):
    newPOL=5
elif(sample=="Business"):
    newPOL=6
elif(sample=="Purchase Of House"):
    newPOL=7
elif(sample=="OTHER"):
    newPOL=8
elif(sample=="Transport & Storage"):
    newPOL=9
elif(sample=="Redemption & Construction"):
    newPOL=10
elif(sample=="Construction"):
    newPOL=11
elif(sample=="Purchasing Of Building Block"):
    newPOL=12
elif(sample=="Business Use only"):
    newPOL=13
elif(sample=="Expansion of Business"):
    newPOL=14
elif(sample=="Agriculture/Farming"):
    newPOL=15
elif(sample=="Furnitures"):
    newPOL=16
elif(sample=="Redemption & Furniture"):
    newPOL=17
elif(sample=="Dairy and Poultry Products"):
    newPOL=18


sample=security[0]
if(sample=="EPF"):
    newSecurity=0
elif(sample=="Mortgage") :
    newSecurity=1
        

sample=CRIB[0]
if(sample=="Over 12 Defaults") :
    newCRIB=1
elif(sample=="Zero Default"):
    newCRIB=2
elif(sample=="Random Default"):
    newCRIB=3
elif(sample=="Non Performing"):
    newCRIB=4
elif(sample==None):
    newCRIB=5
else:
    newCRIB=0
	

sample=TOE[0]
if(sample=="Business/SME"):
    newTOE=0
elif(sample=="Individual person") :
    newTOE=1
elif(sample=="Corporate Entity"):
    newTOE=2

sample=tax[0]
if(sample=="Yes"):
    newTax=0
elif(sample=="No") :
    newTax=1

               
getData=[ammount,period,emi,newPOL,newSecurity,newCRIB,newTOE,POS,assets,loanI,newTax]
sum=0
for i in range(len(getData)):
    sum=sum+getData[i]
tList=(ammount[0]/sum,period[0]/sum,emi[0]/sum,newPOL/sum,newSecurity/sum,newCRIB/sum,newTOE/sum,POS[0]/sum,assets[0]/sum,loanI[0]/sum,newTax/sum)


testdata=pd.DataFrame(tList)
tList=np.array(tList)
tList=tList.reshape(1,-1)
p=loaded_model.predict(tList)

jj=None
if(p[0]=="Notok"):
    jj="Notok"
elif(p[0]=="ok"):
    jj="ok"	


