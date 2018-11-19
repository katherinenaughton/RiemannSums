
function=input("Please input a function: ")
x1=int(input("Where would you like your interval to start? "))
x2=int(input("Where would you like your interval to end? "))
rectangles=int(input("How many rectangles would you like to have? "))

width=(x2-x1)/rectangles

xcoord=[]

ycoordlist=[]                               #This prints a list of the y values. 
for r in range(x1, x2+1):
    x=r
    Locfunction=function.lower()
    y=eval(Locfunction)
    ycoordlist.append(y)
#print(ycoordlist)

for r in range 





