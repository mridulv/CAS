from numpy import *

def test(a,o):
    print o
    m=0
    l=0
    for i in range(o):
      m=0
      if a[i,i]==0:
        l=1
        for j in range(i,o):
            if a[i,i]==0:
                m=1    
                a[i,i]=a[i,i]+a[j,i]
            if a[i,i]!=0:
                m=0
                break
      if m==0:   
          if l==1:
            for k in range(o):
                    if k==i:
                        continue
                    a[i,k]=a[i,k]+a[j,k]
          c=a[i,i]

          for j in range(i+1,o):
                 v=a[j,i]
                 for k in range(i,o):
                        a[j,k]=a[j,k]-v*a[i,k]/c
                        print a

    
    return a
