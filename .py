'''
Katie, Ella, Alice, Ingrid
'''

from math import sin, cos, tan, acos, asin, atan, exp, e, pi, log, log10, sqrt, log2

L=0#LRAM
M=0#MRAM
R=0#RRAM
S=0#Simpsons

n = int(input("Rectangles"))
function = input("Function")
start = float(input("Start"))
end = float(input("End"))

width = (end - start)/float(n)

for i in range(n):
    temp = 0
    x = start + i*width
    L += eval(function)*width
    temp += eval(function)
    
    x = start + (i+0.5)*width
    M += eval(function)*width
    temp += 4*eval(function)
    
    x = start + (i+1)*width
    R += eval(function)*width
    temp += eval(function)
    
    S += (temp)*width/(2*3)
    
print("LRAM: ",L)
print("MRAM: ",M)
print("RRAM: ",R)
print("Trapezoid :",(L+R)/2)
print("Simpson's Method: ", S)