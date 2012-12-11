from numpy import *
from numpy import transpose

def proj(vec1,vec2,s):
    val=[0]*s
    ip1=0
    for i in range(s):
        ip1=ip1+vec1[i]*vec2[i]
    ip2=0
    for i in range(s):
        ip2=ip2+vec1[i]*vec1[i]
    for i in range(s):
        val[i]=(-1)*(ip1/ip2)*vec1[i]
    return val   
def add(vec1,vec2,s):
    val=[0]*s
    for i in range(s):
        val[i]=vec1[i]+vec2[i]
    return val

def gram(v,s,n):
    u=[[0]*s for i in range(n)]
    u[0]=v[0]
    for k in range(1,n):
        tmp=[0]*s
        for i in range(k):
            tmp=add(tmp,proj(u[i],v[k],s),s)
        u[k]=add(v[k],tmp,s)
    return u
def ortho(u,s,n):
    for i in range(n):
        mag=0
        for k in range(s):
            mag=mag+u[i][k]**2
        mag=(mag)**.5
        for k in range(s):
            u[i][k]=u[i][k]/mag
    return u       

"""print('input the order of matrix')
n=int(raw_input())

m=[[0]*n for i in range(n)]
l=[[0]*n for i in range(n)]
for i in range(n):
    print 'input the row-',i
    exp=raw_input()
    for j in range(n):
        m[i][j]=float(exp.split()[j])
        l[i][j]=float(exp.split()[j])"""

def test(exp):
    m=eval(exp)
    l=eval(exp)
    n=len(m)
    for i in range(n):
        for j in range(n):
            m[i][j]=float(m[i][j])
            l[i][j]=float(l[i][j])
            #if i<j:
                #m[i][j],m[j][i]=m[j][i],m[i][j]
                #l[i][j],l[j][i]=l[j][i],l[i][j]
    l=array(l)  
    q=gram(m,n,n)
    q=ortho(q,n,n)
    q=array(q)
    print('matrix Q is')
    print  q.transpose()
    print dot(q.transpose(),q)
    l=array(l)
    r=dot(q,l)
    print('matrix R is')
    print  r
    print dot(q,r)
    return q,r


