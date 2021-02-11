from numpy import *
print("Programmed by 'NAVDEEP MEHTA'")
print("Under the guidance of 'Kumar Kaushik Ranjan Sir'")
print("It will solve upto n variable equation")
import math
def scanf(equ):
    n=int(input("enter the nunber equation "))
    for i in range (0,n) :
        equ.append([])
    for i in range (0,n) :
        for j in range (0,n):
            equ[i].append(j)
            equ[i][j]=0
            print (f"enter the value of equation {i+1} value of x{j+1} after ")
            equ[i][j]=float(input())
    return n 
def scanfconst(const,n)  :
    for i in range (0,n) :
        const.append([])
    for i in range (0,n) :
        for j in range (0,1):
            const[i].append(j)
            const[i][j]=0
            print (f'enter the value of constant {i+1} value of b{j+1}') 
            const[i][j]=float(input())         
def printf(equ,show):
    if show==1:
        print("matrix is")
        print(equ)
    elif show==2   :
        print("inverse matrix is ")
        print(equ) 
def minor(b,equ,i,n):
    h=0
    k=0 
    for l in range(1,n)  :
        for j in range (0,n):
            if j==i :
                continue
            b[h][k]=equ[l][j]
            k=k+1
            if k==(n-1) :
                h=h+1
                k=0 
def det(equ,n):
    b=[]
    for i in range (0,n) :
        b.append([])
    for i in range (0,n) :
        for j in range (0,n):
            b[i].append(j)
            b[i][j]=0
    sum=0
    if n==1:
        s=equ[0][0]
        return s    
    elif n==2:
        s1=equ[0][0]*equ[1][1]-equ[0][1]*equ[1][0]     
        return s1
    else :
        for i in range (0,n):
            minor(b,equ,i,n)
            sum=float((sum+equ[0][i]*pow(-1,i)*det(b,(n-1))))
        return sum
def transpose(c,d,n,det):
    b=[]
    for i in range (0,n) :
        b.append([])
    for i in range (0,n) :
        for j in range (0,n):
            b[i].append(j)   
            b[i][j]=0
            b[i][j] = c[j][i]
    for i in range (0,n):
        for j in range (0,n):
            d[i][j] = b[i][j]/det
def cofactor(equ,d,n,determinte):
    b=[]
    c=[]
    for i in range (0,n) :
        b.append([])
    for i in range (0,n) :
        for j in range (0,n):
            b[i].append(j)
            b[i][j]=0
    for i in range (0,n) :
        c.append([])
    for i in range (0,n) :
        for j in range (0,n):
            c[i].append(j)
            c[i][j]=0 
    for h in range (0,n):
        for l in range(0,n):
            m=0
            k=0
            for i in range (0,n):
                for j in range (0,n):
                    if i != h and j != l :
                        b[m][k]=equ[i][j]
                        if (k<(n-2)) :
                            k=k+1
                        else :
                            k=0
                            m=m+1
            c[h][l] = float(pow(-1,(h+l))*det(b,(n-1))) 
    transpose(c,d,n,determinte)
def inverse(equ,d,n,det):
    if det==0:
        print("Inverse of matrix is not possible")
    elif n==1:
        d[0][0]=1
    else:
        cofactor(equ,d,n,det)
def multiplication(m1,m2):
    m3=[]
    for i in range (len(m1)) :
        m3.append([])
    for i in range (len(m1)) :
        for j in range (len(m2)):
            m3[i].append(j)
            m3[i][j]=0
    for i in range(len(m1)):
        for j in range (len(m2[0])):
            for k in range (len(m2)):
                m3[i][j]= m3[i][j] + m1[i][k] * m2[k][j]
    return m3
equ=[]
const=[]
equ1=[]
equ2=[]
d=[]
n=scanf(equ)
scanfconst(const,n)
for i in range (0,n) :
    d.append([])
for i in range (0,n) :
    for j in range (0,n):
        d[i].append(j)
        d[i][j]=0
printf(equ,1) 
for i in range (0,n) :
    equ.append([])
for i in range (0,n) :
    for j in range (n,n+1):
        equ[i].append(j)
        equ[i][j]=0
        equ[i][j]=const[i][0]      
print(f' matrix with constant value is \n{equ}')
for k in range (1,n) :
    for i in range(k,n) :
        l=k-1
        x=(equ[i][l])/equ[l][l]
        for j in range(k-1,n+1):
            equ[i][j]=equ[i][j]-equ[l][j]*x
print(f' upper matrix variable with constant value is \n{equ}')
for i in range (0,n) :
    equ1.append([])
for i in range (0,n) :
    for j in range (0,n):
        equ1[i].append(j)
        equ1[i][j]=equ[i][j]
print(f'upper matrix variable value is \n{equ1}')
for i in range (0,n) :
    equ2.append([])
for i in range (0,n) :
    for j in range (0,1):
        equ2[i].append(j)
        equ2[i][j]=equ[i][n]
print(f'upper matrix constant value is \n{equ2}')  
deter=det(equ1,n)
print("Inverse of upper matrix is")
inverse(equ1,d,n,deter)
print(d)
m3=multiplication(d,equ2)
print("value of")
for i in range (0,n):
    print(f'x{i+1} = {m3[i][0]}\n')
print("Programmed by 'NAVDEEP MEHTA'")
print("Under the guidance of 'Kumar Kaushik Ranjan Sir'")
input("press enter to close") 