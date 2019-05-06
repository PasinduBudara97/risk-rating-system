
setPOL(POL)
setSecurity(security)
setCRIB(CRIB)            
setTOE(TOE)
setTax(tax)

  
getData=[ammount,period,emi,newPOL,newSecurity,newCRIB,newTOE,POS,assets,loanI,newTax]
list1=[]
for k in range(len(getData[0])):
    i=k+1
    x=[int(getData[0][i]),int(getData[1][i]),int(getData[2][i]),int(getData[3][k]),int(getData[4][k]),int(getData[5][k]),int(getData[6][k]),int(getData[7][i]),int(getData[8][i]),int(getData[9][i]),int(getData[10][k])]
    tot=0
    for j in range(len(x)):
        tot=float(tot)+x[j]
    x=[int(getData[0][i])/tot,int(getData[1][i])/tot,int(getData[2][i])/tot,int(getData[3][k])/tot,int(getData[4][k])/tot,int(getData[5][k])/tot,int(getData[6][k])/tot,int(getData[7][i])/tot,int(getData[8][i])/tot,int(getData[9][i])/tot,int(getData[10][k])/tot,'Notok']
    list1.append(x)
