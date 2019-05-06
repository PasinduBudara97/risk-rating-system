
def setTax(tax):        
   
def setSecurity(security):
    for i in range(len(security)):
        sample=security[i+1]
        if(sample=="EPF"):
            newSecurity.append(0)
        elif(sample=="Mortgage") :
            newSecurity.append(1)

def setCRIB(CRIB):        
    for i in range(len(CRIB)):
        sample=CRIB[i+1]
        if(sample=="Over 12 Defaults") :
            newCRIB.append(1)
        elif(sample=="Zero Default"):
            newCRIB.append(2)
        elif(sample=="Random Default"):
            newCRIB.append(3)
        elif(sample=="Non Performing"):
            newCRIB.append(4)
        elif(sample==None):
            newCRIB.append(5)
        else:
            newCRIB.append(0)

def setTOE(TOE):
    for i in range(len(TOE)):
        sample=TOE[i+1]
        if(sample=="Business/SME"):
            newTOE.append(0)
        elif(sample=="Individual person") :
            newTOE.append(1)
        elif(sample=="Corporate Entity"):
            newTOE.append(2)
 for i in range(len(tax)):
        sample=tax[i+1]
        if(sample=="Yes"):
            newTax.append(0)
        elif(sample=="No") :
            newTax.append(1)