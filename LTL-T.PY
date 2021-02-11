print("Programmed by 'NAVDEEP MEHTA'")
print("Under the guidance of 'Kumar Kaushik Ranjan Sir'")
print("It will solve upto n number of variable equation")
n=int(input("Enter the vaue of n for n*n matrix= "))
import math
equ=[] 
diag=[]
lower=[]
lowerD=[]
upper=[]
for i in range (0,n) :
    equ.append([])
for i in range (0,n) :
    for j in range (0,n):
        equ[i].append(j)
        equ[i][j]=0
        print (f"enter the value of equation {i+1} value of x{j+1} after entering all three value enter b{i+1}")
        equ[i][j]=float(input())      
print(equ)
for i in range (0,n) :
    lower.append([])
for i in range (0,n) :
    for j in range (0,n):
        lower[i].append(j)
        lower[i][j]=0
for i in range (0,n) :
    diag.append([])
for i in range (0,n) :
    for j in range (0,n):
        diag[i].append(j)
        diag[i][j]=0      
for i in range (0,n) :
    lowerD.append([])
for i in range (0,n) :
    for j in range (0,n):
        lowerD[i].append(j)
        lowerD[i][j]=0          
for i in range (0,n) :
    upper.append([])
for i in range (0,n) :
    for j in range (0,n):
        upper[i].append(j)                         
for i in range(n):  
    for j in range(i + 1):  
        sum1 = 0; 
        if (j == i):  
            for k in range(j): 
                sum1 += pow(lower[j][k], 2); 
            lower[j][j] = math.sqrt(equ[j][j] - sum1); 
        else: 
            for k in range(j): 
                sum1 += (lower[i][k] *lower[j][k]); 
            if(lower[j][j] > 0): 
                lower[i][j] = (equ[i][j] - sum1) / lower[j][j];       
for i in range (0,n) :
    for j in range (0,n):
        upper[j][i]=lower[i][j]
for i in range (0,n):
    for j in range (0,n):
        if i==j:
            lowerD[i][j]=1
        elif i<j :
            lower[i][j]=0
        else:
            lowerD[i][j]=lower[i][j]
print("Lower matrix is....") 
print(lowerD)
for i in range (0,n):
    for j in range (0,n):
        if i==j:
            diag[i][j]=lower[i][j]
        elif i<j :
            diag[i][j]==0
        else:
            diag[i][j]=0
print("Diagonal matrix is ....")
print(diag)
for i in range (0,n):
    for j in range (0,n):
        if i==j:
            upper[i][j]=1
        elif i<j :
            upper[i][j]=upper[i][j]
        else:
            upper[i][j]=0
print("Upper matrix is....")            
print(upper)
print("Programmed by 'NAVDEEP MEHTA'")
print("Under the guidance of 'Kumar Kaushik Ranjan Sir'")    
input("press enter to close")               