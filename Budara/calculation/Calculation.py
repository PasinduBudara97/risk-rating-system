
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np
import xlsxwriter




df = pd.read_excel('Interest.xlsx',sheet_name='Sheet1')
writer = xlsxwriter.Workbook('test.xlsx')
worksheet = writer.add_worksheet()
businessExp=df['period of service']
entity=df['type of entity']
tax=df['tax paying']
purpose=df['Purpose of Loan']
security=df['Security type']
exp=df['period of service']

size=len(businessExp)
print(businessExp)




def funBusinessExperience(businessExp):
    i=0
    row = 0

    while i<size:
        print(businessExp[i])
        if(businessExp[i]<1.0):
            expScore[i]=0
        elif(businessExp[i]<=2.0):
            expScore=20
        elif(businessExp[i]<=3.0):
            expScore=30
        elif(businessExp[i]<=4.0):
           expScore=50
        elif(businessExp[i]>5.0):
            expScore=50
        print(expScore)

        worksheet.write(i,1,expScore)

        i+=1
    #writer.close()
    print("hiiiiiiiiiiiiiii")




def funEntityTax(entity,tax):
    i=0
    row = 0

    while i<size:
        if ((entity[i] == "Individual person") & (tax[i] == "Yes")):
            score = 40
        elif ((entity[i] == "Individual person") & (tax[i] == "No")):
            score = 10
        elif ((entity[i] == "Business/SME") & (tax[i] == "Yes")):
            score = 40
        elif ((entity[i] == "Business/SME") & (tax[i] == "No")):
            score = 20
        worksheet.write(i, 2, score)
        i += 1

    print("Successfully added entity and tax" )


def funLoanPurpose(purpose):
    i=0
    while i<size:
        if (purpose[i] == "Construction"):
            escore = 40
        elif (purpose[i] == "OTHER"):
            escore = 20
        elif (purpose[i] == "Business"):
            escore = 20
        elif (purpose[i] == "Purchase"):
            escore = 30
        elif (purpose[i] == "Redemption & Furniture"):
            escore = 10
        elif (purpose[i] == "Redemption & Construction"):
            escore = 10
        elif (purpose[i] == "Renovation/Repair(Improvement)"):
            escore = 40
        elif (purpose[i] == "Purchase Of House"):
            escore = 30
        elif (purpose[i] == "Furnitures"):
            escore = 50
        elif (purpose[i] == "Transport & Storage"):
            escore = 20
        elif (purpose[i] == "Purchasing Of Building Block"):
            escore = 30
        worksheet.write(i, 3, escore)
        i += 1
    print("Successfully added purpose")


def funSecurity(security):
    i=0
    while i<size:
        if (security[i] == "Mortgage"):
            score = 100
        elif (security[i] == "Bank Gurantee"):
            score = 100
        elif (security[i] == "Machineries"):
            score = 80
        elif (security[i] == "Vehicles"):
            score = 70
        elif (security[i] == "Stock or Trade Debtors"):
            score = 50
        elif (security[i] == "Loan Portfolio"):
            score = 50
        elif (security[i] == "Corporate Gurantee"):
            score = 40
        elif (security[i] == "Personal Gurantee"):
            score = 20
        elif (security[i] == "EPF"):
            score = 20
        worksheet.write(i, 4, score)
        i += 1

    print("successfully added security")


def funExperience(exp):
    i=0

    while i<size:
        if (exp[i] < 1):
            score = 0
        elif (exp[i] <= 2):
            score = 20
        elif (exp[i] <= 3):
            score = 30
        elif (exp[i] <= 4):
            score = 40
        elif (exp[i] > 4):
            score = 50
        worksheet.write(i, 5, score)
        i += 1

    print("successfully added experience")

funBusinessExperience(businessExp)
funEntityTax(entity, tax)
funExperience(exp)
funLoanPurpose(purpose)
funSecurity(security)
writer.close()


    # def funCrib(crib):
    #     if (crib== 0):
    #         cribScore = 150
    #     elif(crib<30):
    #         cribScore=125
    #     elif(crib<60):
    #         cribScore=75
    #     else:
    #         cribScore=0
    #
    # def funGearing(gearing):
    #     if(gearing<0.50):
    #         gearingScore=100
    #     elif(gearing<0.60):
    #         gearingScore=70
    #     elif(gearing<0.70):
    #         gearingScore=50
    #     elif(gearing<0.80):
    #         gearingScore=20
    #     else:
    #         gearingScore==0
    #
    # def funDebtServiceCovergae(debt):
    #     if(debt<1.00):
    #         debtScore=20
    #     elif(debt<1.50):
    #         debtScore=50
    #     elif(debt<2.00):
    #         debtScore=75
    #     elif(debt<2.50):
    #         debtScore=100
    #     elif(debt<100):
    #         debtScore=100
    #
    # def funSecurity(security):
    #     if(security=="mortgage"):
    #         secScore=100
    #     elif(security=="bank gurantee"):
    #         secScore=100
    #     elif(security=="machineries"):
    #         secScore=80
    #     elif(security=="70"):
    #         secScore=100
    #     elif(security=="stock or trade debtors"):
    #         secScore=50
    #     elif(security=="loan portfolio"):
    #         secScore=50
    #     elif(security=="corporate portfolio"):
    #         secScore=40
    #     elif(security=="personal guarantee"):
    #         secScore=20
# def funBusinessExperience(businessExp):
#
#     for i in businessExp:
#         print(businessExp)
#         if(businessExp<1):
#             expScore=0
#         elif(businessExp<=2):
#             expScore=20
#         elif(businessExp<=3):
#             expScore=30
#         elif(businessExp<=4):
#            expScore=50
#         else:
#             expScore=50
#         print(expScore)


    # def funPurpose(purpose):
    #     if(purpose=="purchase of machineries"):
    #         purposeScore=50
    #     elif(purpose=="Reinvestments"):
    #         purposeScore=40
    #     elif(purpose=="Purchase of Building"):
    #         purposeScore=30
    #     elif(purpose=="Working Capital "):
    #         purposeScore=20
    #     elif(purpose=="Redemption of Loans"):
    #         purposeScore=10
    #     else:
    #         purposeScore=20
    #
    #
    # def funPoints(self):
    #     totalScore=cribscore+gearingScore+\
    #                debtScore+secScore+expScore+purposeScore;
    #
    #

