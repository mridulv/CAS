from numpy import *
from numpy import transpose
import math

def theta(m,p,q):
    if(m[q][q]!=m[p][p]):
        #print m[p][q]
        return math.atan(2*m[p][q]/(m[q][q]-m[p][p]))/2
    else:
        return (math.pi)/4

def jac_mat(m,n,p,q,t):
    j=[[0]*n for i in range(n)]
    for i in range(n):
        j[i][i]=1
    j[p][p]=math.cos(t)
    j[p][q]=math.sin(t)
    j[q][p]=-math.sin(t)
    j[q][q]=math.cos(t)
    return j
"""print('input the order of matrix')
n=int(raw_input())

m=[[0]*n for i in range(n)]

for i in range(n):
    print 'input the row-',i
    exp=raw_input()
    for j in range(n):
        m[i][j]=float(exp.split()[j])
"""


def test(exp):
    m=eval(exp)
    l=eval(exp)
    n=len(m)
    for i in range(n):
        for j in range(n):
            m[i][j]=float(m[i][j])
            l[i][j]=float(l[i][j])
        
    evector=[[0]*n for i in range(n)]
    for i in range(n):
        evector[i][i]=1
    #evector=matrix(evector)
    m=array(m)
    y=array(m)
    evector=array(evector)
    for l in range(4):
        for i in range(n):
            for k in range(i+1,n):
                t=theta(m,i,k)
                j=array(jac_mat(m,n,i,k,t))
                evector=dot(evector,j)
                #print('P-'),i+k
                #print evector
                m=dot(dot(j.transpose(),m),j)
                #print('m-'),i+k
                #print m
    a=[None]*n            
    print('eigen-vectors are')
    for i in range(n):
        a[i]=evector[i]
    return a
