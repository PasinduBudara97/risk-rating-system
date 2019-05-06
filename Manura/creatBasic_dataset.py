
def createBasicDataset(POL,security,CRIB,TOE,tax):
    #print(POL,security,CRIB,TOE,tax)
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