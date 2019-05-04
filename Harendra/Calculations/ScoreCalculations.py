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
        cribScore = 0
