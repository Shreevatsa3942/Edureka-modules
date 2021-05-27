import pandas as pd

df = pd.read_csv('FairDealCustomerData.csv',header=None)
df[1] = df[1]+" "+df[2]
del df[0]

#print(df[1])
fairCustList = list(df[df[3]==0][1].str.strip())
blockcustlist= list(df[df[3]==1][1].str.strip())

#print(fairCustList)
#print(blockcustlist)
class customer:
    customers = []
    def __init__(self,custlst):
        self.customers = custlst
    def __del__(self):
        self.customers =[]
    def IsFair(self,name):
        #print(self.customers)
        if name in self.customers:
            print('{0} is a fair customer'.format(name))
        else:
            raise Exception


try:
    fr = customer(fairCustList)
    fr.IsFair(input('Enter Customer Name for an Order:'))
    #print(fr.customers)

except:
    print('Sorry!!Input Customer is a blacklisted.')