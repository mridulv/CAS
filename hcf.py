import math

def test(a,b):
    c=a%b
    while c!=0:
        m=b
        b=a%b
        a=m
        c=a%b
    return b

a=test(10,5)
print a
