function=input("Please input a function: ")
x1=int(input("Where would you like your interval to start? "))
x2=int(input("Where would you like your interval to end? "))
rectangles=int(input("How many rectangles would you like to have? "))

width=(x2-x1)/rectangles


ycoordlistL=[]                               #This prints a list of the y values. 
for r in range(x1, x2):
    x=r
    Locfunction=function.lower()
    y=eval(Locfunction)
    ycoordlist.append(y)
print(ycoordlistL)

ycoordlistR=[]                               #This prints a list of the y values. 
for r in range(x1-1, x2+1):
    x=r
    Locfunction=function.lower()
    y=eval(Locfunction)
    ycoordlist.append(y)
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
    ycoordlist.append(y)
print(ycoordlistM)

Larealist=[]
for r in range(x1, x2+1):
    area=ycoordlistL[r]*width
    arealist.append(area)
print(Larealist)

Rarealist=[]
for r in range(x1, x2+1):
    area=ycoordlistR[r]*width
    arealist.append(area)
print(Rarealist)

Marealist=[]
for r in range(x1, x2+1):
    area=ycoordlistM[r]*width
    arealist.append(area)
print(Marealist)

Lsum=sum(Marealist)
print(Lsum)

Rsum=sum(Rarealist)
print(Rsum)

Msum=sum(Marealist)
print(Msum)




