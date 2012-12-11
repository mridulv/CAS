from math import *
from Polynomial_final import *
            
def main(a,order):
    d=[0]*(m+1)
    k=0
    b=[0]*(m+1)
    c=[0]*(m+1)
    x=[0]*(m+1)
    print d,b,c,x
    for i in range(order+1):
        if i==0:
            print a[i]
            tmp=a[i]
            a[i]=1.0
        else:
            a[i]=a[i]/float(tmp)
            d[i]=a[i]
    print 'a is',a,'d is',d
    b[0]=1.0
    c[0]=1.0
    n=order
    precision_error_flag=0
    while n > 2:
        r = 0
        s = 0
        dr = 1.0
        ds = 0
        eps = 1e-14
        iter = 1

        while fabs(dr)+fabs(ds) > eps: 
            if iter % 200 == 0:
                r=rand()/16000.
            if ((iter % 500) == 0): 
                eps=eps*10.0
                precision_error_flag=1
            b[1] = a[1] - r
            c[1] = b[1] - r

            for i in range(2,n+1):
                b[i] = a[i] - r*b[i-1] - s*b[i-2]
                c[i] = b[i] - r*c[i-1] - s*c[i-2]
            dn=c[n-1] * c[n-3] - c[n-2]*c[n-2]
            drn=b[n] * c[n-3] - b[n-1]*c[n-2]
            dsn=b[n-1] * c[n-1] - b[n]*c[n-2]

            if fabs(dn) < 1e-16:
                dn = 1
                drn = 1
                dsn = 1
            dr = drn / dn
            ds = dsn / dn

            r += dr
            s += ds
            iter=iter+1
        for i in range(n): 
            a[i] = b[i]
        a[n] = s
        a[n-1] = r
        print 'a is ',a
        n=n-2
    p=0;
    for i in range(order,0,-2):
         w=a[i-1]
         x=a[i]
         l=w*w-4*x;
         print 'w is ',w,'x is ',x
         if l>=0.001:
           q=(-x+sqrt(l))/2
           e=(-x-sqrt(l))/2
           x.append(q)
           x.append(e)
           print '2'
         print 'x is',x
    if n % 2== 1:
            x.append(a[1])
        
    return c



poly=[]
polynom='x^2+2x+1'
b=Polynomial()
poly=b.definePoly(polynom)
m=b.degreeOfPolynomial(poly)
print poly
z=[0]*(m+1)
print z
for i in range(m+1):
    z[i]=poly[m-i]
    print z[i]
print z
c=main(z,m)
print c
