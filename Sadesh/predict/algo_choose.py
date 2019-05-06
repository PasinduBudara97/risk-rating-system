
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

	

df=pd.read_excel('/home/Desktop/info.xlsx',index_col=0)
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


setPOL(POL)
setSecurity(security)
setCRIB(CRIB)            
setTOE(TOE)
setTax(tax)

getData=[ammount,period,emi,newPOL,newSecurity,newCRIB,newTOE,POS,assets,loanI,newTax]

list2=[]
k=0
for k in range(1476):
	 i=k+1
    x=[int(getData[0][i]),int(getData[1][i]),int(getData[2][i]),int(getData[3][k]),int(getData[4][k]),int(getData[5][k]),int(getData[6][k]),int(getData[7][i]),int(getData[8][i]),int(getData[9][i]),int(getData[10][k])]
    if(k==0):
        print(x)
		
		
  
    tot=0
    for j in range(len(x)):
        tot=float(tot)+x[j]
    x=[int(getData[0][i])/tot,int(getData[1][i])/tot,int(getData[2][i])/tot,int(getData[3][k])/tot,int(getData[4][k])/tot,int(getData[5][k])/tot,int(getData[6][k])/tot,int(getData[7][i])/tot,int(getData[8][i])/tot,int(getData[9][i])/tot,int(getData[10][k])/tot,'ok']
    list2.append(x)

