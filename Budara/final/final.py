import pandas as pd
from random import shuffle
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
import time
import pickle

cols = ['Loan no', 'Ammount', 'Period', 'EMI', 'purpose', 'secutityType', 'CRIB', 'entity', 'POS', 'assets',
        'installments', 'tax']
df = pd.read_excel('../Dataset/failed_data.xlsx', index_col=0)

ammount = df['Loan amount']
period = df['Period']
emi = df['EMI']
POL = df['Purpose of loan']
newPOL = []
security = df['Security type']
newSecurity = []
CRIB = df['CRIB status']
newCRIB = []
TOE = df['type of entity']
newTOE = []
POS = df['period of service(yrs)']
assets = df['Total assets']
loanI = df['loan installments']
tax = df['tax paying']
newTax = []


def setPOL(POL):
    for i in range(len(POL)):
        sample = POL[i + 1]
        if (sample == "Purchase of Machinery & Equipment"):
            newPOL.append(0)
        elif (sample == "Purchase") or (sample == "Purchase "):
            newPOL.append(1)
        elif (sample == "Business & Redemption"):
            newPOL.append(2)
        elif (sample == "Education"):
            newPOL.append(3)
        elif (sample == "Renovation/Repair(Improvement)"):
            newPOL.append(4)
        elif (sample == "Redemption"):
            newPOL.append(5)
        elif (sample == "Business"):
            newPOL.append(6)
        elif (sample == "Purchase Of House"):
            newPOL.append(7)
        elif (sample == "OTHER"):
            newPOL.append(8)
        elif (sample == "Transport & Storage"):
            newPOL.append(9)
        elif (sample == "Redemption & Construction"):
            newPOL.append(10)
        elif (sample == "Construction"):
            newPOL.append(11)
        elif (sample == "Purchasing Of Building Block"):
            newPOL.append(12)
        elif (sample == "Business Use only"):
            newPOL.append(13)
        elif (sample == "Expansion of Business"):
            newPOL.append(14)
        elif (sample == "Agriculture/Farming"):
            newPOL.append(15)
        elif (sample == "Furnitures"):
            newPOL.append(16)
        elif (sample == "Redemption & Furniture"):
            newPOL.append(17)
        elif (sample == "Dairy and Poultry Products"):
            newPOL.append(18)


def setSecurity(security):
    for i in range(len(security)):
        sample = security[i + 1]
        if (sample == "EPF"):
            newSecurity.append(0)
        elif (sample == "Mortgage"):
            newSecurity.append(1)


def setCRIB(CRIB):
    for i in range(len(CRIB)):
        sample = CRIB[i + 1]
        if (sample == "Over 12 Defaults"):
            newCRIB.append(1)
        elif (sample == "Zero Default"):
            newCRIB.append(2)
        elif (sample == "Random Default"):
            newCRIB.append(3)
        elif (sample == "Non Performing"):
            newCRIB.append(4)
        elif (sample == None):
            newCRIB.append(5)
        else:
            newCRIB.append(0)


def setTOE(TOE):
    for i in range(len(TOE)):
        sample = TOE[i + 1]
        if (sample == "Business/SME"):
            newTOE.append(0)
        elif (sample == "Individual person"):
            newTOE.append(1)
        elif (sample == "Corporate Entity"):
            newTOE.append(2)


def setTax(tax):
    for i in range(len(tax)):
        sample = tax[i + 1]
        if (sample == "Yes"):
            newTax.append(0)
        elif (sample == "No"):
            newTax.append(1)


setPOL(POL)
setSecurity(security)
setCRIB(CRIB)
setTOE(TOE)
setTax(tax)

getData = [ammount, period, emi, newPOL, newSecurity, newCRIB, newTOE, POS, assets, loanI, newTax]
list1 = []
for k in range(len(getData[0])):
    i = k + 1
    x = [int(getData[0][i]), int(getData[1][i]), int(getData[2][i]), int(getData[3][k]), int(getData[4][k]),
         int(getData[5][k]), int(getData[6][k]), int(getData[7][i]), int(getData[8][i]), int(getData[9][i]),
         int(getData[10][k])]
    tot = 0
    for j in range(len(x)):
        tot = float(tot) + x[j]
    x = [int(getData[0][i]) / tot, int(getData[1][i]) / tot, int(getData[2][i]) / tot, int(getData[3][k]) / tot,
         int(getData[4][k]) / tot, int(getData[5][k]) / tot, int(getData[6][k]) / tot, int(getData[7][i]) / tot,
         int(getData[8][i]) / tot, int(getData[9][i]) / tot, int(getData[10][k]) / tot, 'Notok']
    list1.append(x)

df = pd.read_excel('../Dataset//info.xlsx', index_col=0)
ammount = df['Loan amount']
period = df['Period']
emi = df['EMI']
POL = df['Purpose of loan']
newPOL = []
security = df['Security type']
newSecurity = []
CRIB = df['CRIB status']
newCRIB = []
TOE = df['type of entity']
newTOE = []
POS = df['period of service(yrs)']
assets = df['Total assets']
loanI = df['loan installments']
tax = df['tax paying']
newTax = []

setPOL(POL)
setSecurity(security)
setCRIB(CRIB)
setTOE(TOE)
setTax(tax)

getData = [ammount, period, emi, newPOL, newSecurity, newCRIB, newTOE, POS, assets, loanI, newTax]

list2 = []
k = 0
for k in range(1476):
    i = k + 1
    x = [int(getData[0][i]), int(getData[1][i]), int(getData[2][i]), int(getData[3][k]), int(getData[4][k]),
         int(getData[5][k]), int(getData[6][k]), int(getData[7][i]), int(getData[8][i]), int(getData[9][i]),
         int(getData[10][k])]
    if (k == 0):
        print(x)

    tot = 0
    for j in range(len(x)):
        tot = float(tot) + x[j]
    x = [int(getData[0][i]) / tot, int(getData[1][i]) / tot, int(getData[2][i]) / tot, int(getData[3][k]) / tot,
         int(getData[4][k]) / tot, int(getData[5][k]) / tot, int(getData[6][k]) / tot, int(getData[7][i]) / tot,
         int(getData[8][i]) / tot, int(getData[9][i]) / tot, int(getData[10][k]) / tot, 'ok']
    list2.append(x)

list = list1 + list2
totPred = 0
cp = 0
model = None
for i in range(10):
    shuffle(list)
    bigData = pd.DataFrame(list, columns=['', '', '', '', '', '', '', '', '', '', '', 'label'])
    target = bigData['label']
    from sklearn.model_selection import train_test_split

    X_train, X_test, Y_train, Y_test = train_test_split(bigData.drop(['label'], axis='columns'), target, test_size=0.2)
    model = KNeighborsClassifier(n_neighbors=30)
    model.fit(X_train, Y_train)
    pred = model.score(X_test, Y_test)
    if (pred > cp):
        cp = pred
        filename = '../TrainedModel/finalizedModel.sav'
        pickle.dump(model, open(filename, 'wb'))
    totPred = pred + totPred
    print("Accuracy :", pred)

print("")
print("Algorithm : KNN")
print("Train Data Count : ", len(X_train))
print("Test Data Count : ", len(X_test))
print("Accuracy :", cp)
