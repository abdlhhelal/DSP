#coded by Abdallah Helal on Sunday, May 31,2020
#this code is for solving signals convolution equations
#with no limits for the number of input signals

import re

class CNV_Type:
    def __init__(self,NCNV,X,Y):
        self.NCNV = NCNV #mode of convolution
        self.X = X #first list of integers
        self.Y = Y #second list of integers
        self.dictR={} #defining a dectionary to be operated into
        for i in range(self.NCNV): #adjusting the length of the dectionary
            self.dictR['R'+str(i)]=[0]*self.NCNV

    def CNV(self):
        for i in range(len(self.X)): #first step of convolution
            for j in range(len(self.Y)):
                self.dictR['R'+str(i)][j]=self.Y[i]*self.X[j]
        for i in range(1,self.NCNV):
            for j in range(i): #adjusting the length of all lists
                self.dictR['R'+str(i)].insert(0,0)
        for i in range(self.NCNV-1):
            for j in range(self.NCNV-1,i,-1):
                self.dictR['R'+str(i)].append(0)
        sum=[0]*((2*self.NCNV)-1)
        for i in range (2*self.NCNV-1):
            for j in range(self.NCNV):
                sum[i]+=self.dictR['R'+str(j)][i] #second step of convolution
        sum.append(0) #third step of convolution
        A=sum[:len(sum)//2]
        B=sum[len(sum)//2:]
        S=zip(A,B)
        sum=[x+y for (x,y) in S]
        print(' %sCNV=['%self.NCNV,end='') #printing the output
        for i in range(len(sum)):
            if not i == len(sum)-1:
                print(str(sum[i])+',',end='')
            else:
                print(str(sum[i])+']')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*.*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        return None

class InputNumbers:
    def __init__(self,Order,NCNV):
        self.Order = Order #first or second
        self.NCNV = NCNV #mode of convolution
    def getValues(self):
        loop=True
        while (loop):
            loop=False
            print('Enter the %s '%self.NCNV + self.Order + ' Numbers :')
            Numbers=input()
            #checking if the numbers are written right or not
            CheckRegex=re.compile(r'^(\s*(-\d|\d)\d*(,|\s)){%s}\s*(-\d|\d)\d*\s*$'%(self.NCNV-1))
            try:
                CheckValid = CheckRegex.search(Numbers).group()
            except:
                print('The %s Numbers must be entered as x,x or x x'%self.NCNV)
                loop=True
        #converting string into list of integers
        ValidNumbers=Numbers.split()
        if len(ValidNumbers) == 1:
            ValidNumbers=Numbers.split(',')
        for i in range(len(ValidNumbers)):
            ValidNumbers[i] = int(ValidNumbers[i])
        return ValidNumbers

def getNCNV():
    loop=True
    while(loop):
        NCNV=0
        loop=False
        print('Enter 2 4 8 16.. for choosing 2CNV 4CNV 8CNV 16CNV.. respectively:')
        CNVMode=input()
        try:#checking if the number of signals are even or not
            if int(CNVMode)%2 == 0 and int(CNVMode)!=0:
                NCNV=int(CNVMode)
            else:
                print('Invalid Number.')
                loop=True
        except:
            print('Invalid Number.')
            loop=True
    return NCNV

while(True):
    NCNV=getNCNV()
    X=InputNumbers('First',NCNV)
    Y=InputNumbers('Second',NCNV)
    C=CNV_Type(NCNV,X.getValues(),Y.getValues())
    C.CNV()
