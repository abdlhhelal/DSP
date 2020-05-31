

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
    while(loop1):
        loop1=False
        print('Please Enter The first numbers:')
        First=input()
        if (First[0].isdecimal()):
            x1=int(First[0])
            if(First[2].isdecimal()):
                x2=int(First[2])
            elif(First[2] == '-'):
                x2=int(First[3])* -1
            else:
                print('Please Enter a Valid Number')
                loop1=True
        elif(First[0] == '-'):
            x1=int(First[1])* -1
            if(First[3].isdecimal()):
                x2=int(First[3])
            elif(First[3] == '-'):
                x2=int(First[4])* -1
            else:
                print('Please Enter a Valid Number')
                loop1=True
        else:
            print('Please Enter a Valid Number')
            loop1=True
    while(loop2):
        loop2=False
        print('Please Enter The second numbers:')
        Second=input()
        if (Second[0].isdecimal()):
            y1=int(Second[0])
            if(Second[2].isdecimal()):
                y2=int(Second[2])
            elif(Second[2] == '-'):
                y2=int(Second[3])* -1
            else:
                print('Please Enter a Valid Number')
                loop2=True
        elif(Second[0] == '-'):
            y1=int(Second[1])* -1
            if(Second[3].isdecimal()):
                y2=int(Second[3])
            elif(Second[3] == '-'):
                y2=int(Second[4]) * -1
            else:
                print('Please Enter a Valid Number')
                loop2=True
        else:
            print('Please Enter a Valid Number')
            loop2=True
    ValidNumbers=[x1,x2,y1,y2]
    return ValidNumbers

VN=getValues()
X=[VN[0],VN[1]]
Y=[VN[2],VN[3]]
CNV2(X,Y)
