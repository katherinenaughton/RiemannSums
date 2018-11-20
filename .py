from math import sin, cos, tan, acos, asin, atan
from math import exp, e, pi
from math import log, log10, sqrt, log2
function=input("Please input a function: ")
x1=int(input("Where would you like your interval to start? "))
x2=int(input("Where would you like your interval to end? "))
rectangles=int(input("How many rectangles would you like to have? "))

width=((x2-x1)/rectangles)
print(width)

xcoordlist=[]
for r in range(x1, x2+1):
    xcoordlist.append(r)
    
lastxcoord=xcoordlist[-1]


lengthx=int(len(xcoordlist))
print(lengthx)

if width!=1:
    xcoordlistL=[]
    for r in range(x1, x2):
        xcoordlistL.append(r)
        xcoordlistL.append(r+width)
    print(xcoordlistL)
    
    xcoordlistR=[]
    for r in range(x1+1, x2):
        xcoordlistR.append(r)
        xcoordlistR.append(r+width)
    print(xcoordlistR)
    
    xcoordlistM=[]
    for r in range (x1, x2):
        x=r+(width/2)
        xcoordlistM.append(x)
    print(xcoordlistM)

else:
    xcoordlist=[]
    for r in range(x1, x2+1):
        xcoordlist.append(r)
    print(xcoordlist)


ycoordlistL=[]                               #This prints a list of the y values. 
for r in range(x1, x2):
    x=r
    Locfunction=function.lower()
    y=eval(Locfunction)
    ycoordlistL.append(y)
print(ycoordlistL)

ycoordlistR=[]                               #This prints a list of the y values. 
for r in range(x1-1, x2+1):
    x=r
    Locfunction=function.lower()
    y=eval(Locfunction)
    ycoordlistR.append(y)
print(ycoordlistR)

xcoordlistM=[]
for r in range (x1, x2):
    x=r+(width/2)
    xcoordlistM.append(x)
print(xcoordlistM)

ycoordlistM=[]                               
for r in xcoordlistM:
    x=r
    Locfunction=function.lower()
    y=eval(Locfunction)
    ycoordlistM.append(y)
print(ycoordlistM)

length=len(ycoordlistL)
Larealist=[]
for r in range(length):
    area=ycoordlistL[r]*width
    Larealist.append(area)
print(Larealist)

Rarealist=[]
for r in range(length):
    area=ycoordlistR[r]*width
    Rarealist.append(area)
print(Rarealist)

Marealist=[]
for r in range(length):
    area=ycoordlistM[r]*width
    Marealist.append(area)
print(Marealist)

Lsum=sum(Marealist)
print(Lsum)

Rsum=sum(Rarealist)
print(Rsum)

Msum=sum(Marealist)
print(Msum)




