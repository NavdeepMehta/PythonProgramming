print("This program doest not run unless and until u do not download 'numpy' and 'scipy' libary ")
from numpy import *
from scipy.linalg import svd
print("Programmed by 'NAVDEEP MEHTA'")
print("Under the guidance of 'Kumar Kaushik Ranjan Sir'")
print("It will solve upto n number of variable equation")
n=int(input("enter the row  "))
m=int(input("enter the coloumn "))
equ=[]
for i in range (0,n) :
    equ.append([])
for i in range (0,n) :
    for j in range (0,m):
        equ[i].append(j)
        equ[i][j]=0
        print (f'enter the value of equation {i+1} value of x{j+1}' )
        equ[i][j]=float(input()) 
print(equ)
equ=matrix(equ)
U, s, VT= svd(equ)        
print(U)
print(s)
print(VT)