import random

def modulo(a,b,c):    
   return (a**b)%c

def millerRabin(N,iteration):    
    if N<2:        
        return False

    if N!=2 and N%2==0:        
        return False

    d=N-1
    s=0
    while d%2==0:        
        d = d/2
        s=s+1

    for i in range(iteration):        
        a = random.randint(1, N-1)
        temp = d
        x = modulo(a,temp,N)
        if x==1 or x==N-1:
            continue
        for r in range(1,s):
            x=modulo(x,2,N)
            if x==1:
                return False
            if x==N-1:
                continue
        return False    
    return True


def prime(N):
    ans=millerRabin(N,5)
    if ans==False:
        text= 'N is Composite'
    if ans==True:
        text='n is probaby prime with probability ',1-4**(-5)

    return text

    print text



