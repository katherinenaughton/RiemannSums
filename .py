'''
Katie, Ella, Alice, Ingrid
'''

function=input("Please input a function: ")
x1=int(input("Where would you like your interval to start? "))
x2=int(input("Where would you like your interval to end? "))
rectangles=int(input("How many shapes would you like to have? "))

width=((x2-x1)/rectangles)
#print(width)


xcoordlist=[]
b=0
for i in range(rectangles+1):
    xcoordlist.append(x1+(b*width))
    b+=1

print("your x=coordinates are: ",xcoordlist)

LRAMxcoord = []
RRAMxcoord = []
MRAMxcoord = []

b=0
for i in range(len(xcoordlist)-1):
    LRAMxcoord.append(xcoordlist[i])

b=1   
for i in xcoordlist:
    s = xcoordlist[b]
    MRAMxcoord.append(i+s/2)

Rxcoordlist = xcoordlist[::-1]  
for i in range(len(xcoordlist)-1):
    RRAMxcoord.append(Rxcoordlist[i])
 

#print(LRAMxcoord)
#print(RRAMxcoord)
#print(MRAMxcoord)


lengthx=int(len(xcoordlist))
#print(lengthx)


ycoordlistL=[]                               #This prints a list of the y values. 
for r in LRAMxcoord:
    x=r
    Locfunction=function.lower()
    y=eval(Locfunction)
    ycoordlistL.append(y)
#print(ycoordlistL)

ycoordlistR=[]                               #This prints a list of the y values. 
for r in RRAMxcoord:
    x=r
    Locfunction=function.lower()
    y=eval(Locfunction)
    ycoordlistR.append(y)
#print(ycoordlistR)

ycoordlistM=[]
for r in MRAMxcoord:
    x=r
    Locfunction=function.lower()
    y=eval(Locfunction)
    ycoordlistM.append(y)
#print(ycoordlistM)


length=len(ycoordlistL)
#print(length)

Larealist=[]
for r in range(length):
    area=ycoordlistL[r]*width
    Larealist.append(area)
#print(Larealist)

Rarealist=[]
for r in range(length):
    area=ycoordlistR[r]*width
    Rarealist.append(area)
#print(Rarealist)

Marealist=[]
for r in range(length):
    area=ycoordlistM[r]*width
    Marealist.append(area)
#print(Marealist)

Lsum=sum(Larealist)
print("Your LRAM sum is", Lsum)

Msum=sum(Marealist)
print("Your MRAM sum is", Msum)

Rsum=sum(Rarealist)
print("Your RRAM sum is", Rsum)

print("Your TRAP sum is", ((Lsum+Rsum)/2))

h = width/2

xcoordlist=[]
b=0
for i in range((2*rectangles)+1):
    xcoordlist.append(x1+(b*h))
    b+=1
    
ycoordlist=[]                               #This makes a list of the y values. 
for r in xcoordlist:
    x=r
    Locfunction=function.lower()
    y=eval(Locfunction)
    ycoordlist.append(y)
    
Sarealist = []    
a = 1
b = 2
c = 0
for f in ycoordlist:
    if b < len(ycoordlist):
        A = ycoordlist[a]
        B = ycoordlist[b]
        C = ycoordlist[c]
        d = (h/3)*(C+(4*A)+B)
        print(d)
        Sarealist.append(d)
        a+=2
        b+=2
        c+=2
    else:
        print()
        
print(sum(Sarealist))
