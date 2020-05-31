import re

class CNV_Type:
    def __init__(self,NCNV,X,Y):
        self.NCNV = NCNV #mode of convolution
        self.X = X #first list of integers
        self.Y = Y #second list of integers
        self.dictR={}
        for i in range(self.NCNV):
            self.dictR['R'+str(i)]=[0]*self.NCNV

    def CNV(self):
        for i in range(len(self.X)):
            for j in range(len(self.Y)):
                self.dictR['R'+str(i)][j]=self.Y[i]*self.X[j]
        for i in range(1,self.NCNV):
            for j in range(i):
                self.dictR['R'+str(i)].insert(0,0)
        for i in range(self.NCNV-1):
            for j in range(self.NCNV-1,i,-1):
                self.dictR['R'+str(i)].append(0)
        sum=[0]*((2*self.NCNV)-1)
        for i in range (2*self.NCNV-1):
            for j in range(self.NCNV):
                sum[i]+=self.dictR['R'+str(j)][i]
        sum.append(0)
        A=sum[:len(sum)//2]
        B=sum[len(sum)//2:]
        S=zip(A,B)
        sum=[x+y for (x,y) in S]
        print('Output is:',end='')
        for i in range(len(sum)):
            print(' '+str(sum[i]),end='')
        return None

class InputNumbers:
    def __init__(self,Order,NCNV):
        self.Order = Order
        self.NCNV = NCNV
    def getValues(self):
        loop=True
        while (loop):
            loop=False
            print('Enter the %s '%self.NCNV + self.Order + ' Numbers :')
            Numbers=input()
            #checking if the numbers are written right or not
            CheckRegex=re.compile(r'^((-|\d)\d*(,|\s)){%s}(-|\d)\d*$'%(self.NCNV-1))
            CheckNum=CheckRegex.search(Numbers)
            try:
                CheckValid = CheckNum.group()
            except:
                print('The %s Numbers must be entered as x,x or x x'%self.NCNV)
                loop=True
        #converting string into list of two integers
        ValidNumbers=Numbers.split()
        if (len(ValidNumbers) == 1):
            ValidNumbers=Numbers.split(',')
        for i in range(len(ValidNumbers)):
            ValidNumbers[i] = int(ValidNumbers[i])
        return ValidNumbers

def getNCNV():
    loop=True
    while(loop):
        NCNV=0
        loop=False
        print('Enter 2 4 8 for choosing 2CNV 4CNV 8CNV respectively:')
        CNVMode=input()
        try:
            if(int(CNVMode)==2):
                NCNV=2
            elif(int(CNVMode)==4):
                NCNV=4
            elif(int(CNVMode)==8):
                NCNV=8
            else:
                print('Invalid Number.')
                loop=True
        except:
            print('Invalid Number.')
            loop=True
    return NCNV

NCNV=getNCNV()
X=InputNumbers('First',NCNV)
Y=InputNumbers('Second',NCNV)
C=CNV_Type(NCNV,X.getValues(),Y.getValues())
C.CNV()
