import re

def CNV2(X,Y):
    R1=[(X[0]*Y[0]),(X[1]*Y[0]),0]
    R2=[0,(X[0]*Y[1]),(X[1]*Y[1])]
    S=zip(R1,R2)
    Sum=[x+y for (x,y) in S]
    R3=[Sum[-1],0,0]
    S=zip(Sum,R3)
    Sum=[x+y for (x,y) in S]
    print('Output is: ' + str(Sum[0]) + ' ' + str(Sum[1]))
    return None

class InputNumbers:
    def __init__(self,Order):
        self.Order= Order

    def getValues(self):
        loop=True
        while (loop):
            loop=False
            print('Enter the '+ self.Order + ' numbers :')
            Numbers=input()
            #checking if the numbers are written right or not
            CheckRegex=re.compile(r'^(-|\d)\d*(,|\s)(-|\d)\d*$')
            CheckNum=CheckRegex.search(Numbers)
            try:
                CheckValid = CheckNum.group()
            except:
                print("Numbers must be entered as x,x or x x")
                loop=True
        #converting string into integers
        ValidNumbers=Numbers.split()
        if (len(ValidNumbers) == 1):
            ValidNumbers=Numbers.split(',')
        for i in range(len(ValidNumbers)):
            ValidNumbers[i] = int(ValidNumbers[i])
        return ValidNumbers

X=InputNumbers("First")
Y=InputNumbers("Second")
CNV2(X.getValues(),Y.getValues())
