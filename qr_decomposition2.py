
#evalue_qr_1

from numpy import *
from numpy import transpose
import copy
def proj(vec1,vec2,n):
    val=[0]*n
    ip1=0
    for i in range(n):
        ip1=ip1+vec1[i]*vec2[i]
    ip2=0
    for i in range(n):
        ip2=ip2+vec1[i]*vec1[i]
    for i in range(n):
        val[i]=(-1)*(ip1/ip2)*vec1[i]
    return val   
def add(vec1,vec2,n):
    val=[0]*n
    for i in range(n):
        val[i]=vec1[i]+vec2[i]
    return val

def gram(v,n):
    u=[[0]*n for i in range(n)]
    u[0]=v[0]
    for k in range(1,n):
        tmp=[0]*n
        for i in range(k):
            tmp=add(tmp,proj(u[i],v[k],n),n)
        u[k]=add(v[k],tmp,n)
    return u

def ortho(u,n):
    for i in range(n):
        mag=0
        for k in range(n):
            mag=mag+u[i][k]**2
        mag=(mag)**.5
        for k in range(n):
            u[i][k]=u[i][k]/mag
    return u       

def qr_dec_q(h,n):
    q=gram(h,n)
    q=ortho(q,n)
    q=array(q)
    return q.transpose()

def test(exp):
    m=eval(exp)
    l=eval(exp)
    n=len(m)
    for i in range(n):
        for j in range(n):
            m[i][j]=float(m[i][j])
            l[i][j]=float(l[i][j])
            if i<j:
                m[i][j],m[j][i]=m[j][i],m[i][j]
                l[i][j],l[j][i]=l[j][i],l[i][j]
    l=array(l)
    a=[None]*n
    for i in range(10):
        Q=qr_dec_q(m,n)
        print 'q is',Q
        l=dot(dot(Q,l),Q.transpose())
        print l
        m=copy.copy(l)

    print ('The eigen-values are')
    for i in range(n):
         a[i]=l[i][i]
    return a    


