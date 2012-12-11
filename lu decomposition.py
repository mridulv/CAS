
from numpy import matrix
from numpy import *

def LUdecomp(a):
    n = len(a)
    for k in range(0,n-1):
        for i in range(k+1,n):
           if abs(a[i,k]) > 1.0e-9:
               lam = a [i,k]/a[k,k]
               a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
               a[i,k] = lam
    return a

def test(a):
    l=zeros((len(b),len(b)))
    d=zeros((len(b),len(b)))
    u=zeros((len(b),len(b)) )       
    b=matrix(b) 
    b=LUdecomp(b)
    for i in range(len(b)):
            for j in range(len(b)):
                if i>j:
                    l[i,j]=b[i,j]
                if j>i:
                    d[i,j]=b[i,j]
                if j==i:
                    d[i,j]=1
                    l[i,j]=1
                    u[i,j]=b[i,j]
    return l,u,d       
                
