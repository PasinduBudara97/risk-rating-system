class Calculation:
    def __init__(self,name,crib,):
        self.name=name
        self.crib = crib
        self.cribScore= none

    def funCrib(crib):
        if (crib== 0):
            cribScore = 150
        elif(crib<30):
            cribScore=125
        elif(crib<60):
            cribScore=75
        else:
            cribScore=0

    def funGearing(gearing):
        if(gearing<0.50):
            gearingScore=100
        elif(gearing<0.60):
            gearingScore=70
        elif(gearing<0.70):
            gearingScore=50
        elif(gearing<0.80):
            gearingScore=20
        else:
            gearingScore==0

    def funDebtServiceCovergae(debt):
        if(debt<1.00):
            debtScore=20
        elif(debt<1.50):
            debtScore=50
        elif(debt<2.00):
            debtScore=75
        elif(debt<2.50):
            debtScore=100
        elif(debt<100):
            debtScore=100

    def funSecurity(security):
        if(security=="mortgage"):
            secScore=100
        elif(security=="bank gurantee"):
            secScore=100
        elif(security=="machineries"):
            secScore=80
        elif(security=="70"):
            secScore=100
        elif(security=="stock or trade debtors"):
            secScore=50
        elif(security=="loan portfolio"):
            secScore=50
        elif(security=="corporate portfolio"):
            secScore=40
        elif(security=="personal guarantee"):
            secScore=20
    def funBusinessExperience(businessExp):
        if(businessExp<=1):
            expScore=0
        elif(businessExp<=2):
            expScore=20
        elif(businessExp<=3):
            expScore=30
        elif(businessExp<=4):
            expScore=50
        elif(businessExp<5):
            expScore=50
        else:
            expScore==100

    def funPurpose(purpose):
        if(purpose=="purchase of machineries"):
            purposeScore=50
        elif(purpose=="Reinvestments"):
            purposeScore=40
        elif(purpose=="Purchase of Building"):
            purposeScore=30
        elif(purpose=="Working Capital "):
            purposeScore=20
        elif(purpose=="Redemption of Loans"):
            purposeScore=10
        else:
            purposeScore=20


    def funPoints(self):
        totalScore=cribscore+gearingScore+\
                   debtScore+secScore+expScore+purposeScore;



