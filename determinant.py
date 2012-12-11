from numpy import *
import gauss

def determinant(a):
    c=matrix(a)
    d=1;
    l=c.T
    if len(l)==len(c):
        b=gauss.test(c,len(a))
        print b
        for i in range(len(a)):
            d=d*b[i,i]
        print d
        return d
    else:
        return 'the matrix is not square'

a=determinant([[1,2,3],[4,5,6],[7,8,9]])
print a 
            
