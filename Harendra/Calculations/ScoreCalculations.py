def __init__(self, name, crib, ):
    self.name = name
    self.crib = crib



def funtionCribScore(crib):
    if (crib == 0):
        cribScore = 150
    elif (crib < 30):
        cribScore = 125
    elif (crib < 60):
        cribScore = 75
    else:
        cribScore=0

def funDebtServiceCovergae(debt):
            if (debt < 1.00):
                debtScore = 20
            elif (debt < 1.50):
                debtScore = 50
            elif (debt < 2.00):
                debtScore = 75
            elif (debt < 2.50):
                debtScore = 100
            elif (debt < 100):
                debtScore = 100
