import re

def CNV2(X,Y):
    R1=[(X[0]*Y[0]),(X[1]*Y[0]),0]
    R2=[0,(X[0]*Y[1]),(X[1]*Y[1])]
    S=zip(R1,R2)
    Sum=[x+y for (x,y) in S]
    R3=[Sum[-1],0,0]
    S=zip(Sum,R3)
    Sum=[x+y for (x,y) in S]
    print('The output is: ' + str(Sum[0]) + ' ' + str(Sum[1]))
    return None

def getValues():
    loop1=True
    loop2=True
    while (loop1):
        loop1=False
        print('Enter the first numbers :')
        Numbers=input()
        #checking if the numbers are written right or not
        CheckRegex=re.compile(r'^(-|\d)\d*(,|.|\s)(-|\d)\d*$')
        CheckNum=CheckRegex.search(Numbers)
        try:
            CheckValid = CheckNum.group()
        except:
            searchbox_result = None
            print("Numbers must be entered as x,x or x x")
            loop1=True
    Num1Regex=re.compile(r'^((-|\d)(\d*))(,|.|\s)')
    SearchNum1=Num1Regex.search(Numbers)
    Num1_1=int(SearchNum1.group(1))
    Num2Regex=re.compile(r'(,|.|\s)((-|\d)(\d*))$')
    SearchNum2=Num2Regex.search(Numbers)
    Num1_2=int(SearchNum2.group(2))
    while (loop2):
        loop2=False
        print('Enter the second numbers:')
        Numbers=input()
        #checking if the numbers are written right or not
        CheckRegex=re.compile(r'^(-|\d)\d*(,|.|\s)(-|\d)\d*$')
        CheckNum=CheckRegex.search(Numbers)
        try:
            CheckValid = CheckNum.group()
        except:
            searchbox_result = None
            print("Numbers must be entered as x,x or x x")
            loop2=True
    Num2Regex=re.compile(r'^((-|\d)(\d*))(,|.|\s)')
    SearchNum2=Num2Regex.search(Numbers)
    Num2_1=int(SearchNum2.group(1))
    Num2Regex=re.compile(r'(,|.|\s)((-|\d)(\d*))$')
    SearchNum2=Num2Regex.search(Numbers)
    Num2_2=int(SearchNum2.group(2))
    ValidNumbers=[Num1_1,Num1_2,Num2_1,Num2_2]
    return ValidNumbers

VN=getValues()
X=[VN[0],VN[1]]
Y=[VN[2],VN[3]]
CNV2(X,Y)
