import math
import cython
import extract
import cmath
import time
def integrate(exp,downer,upper):
        if(upper=='inf'):
            upper=100000
        if(exp.isnumeric()):
            return(int(exp)*(upper-downer))
        dx=(upper-downer)/1000
        val1=cython.declare(cython.float)
        val2=cython.declare(cython.float)
        arr=[0]
        if(upper==downer):
            sum=0.0
        elif(upper>downer):
            j=downer
            sum=0.0
            while(j<upper):
                arr[0]=j
                val1=extract.main(exp,arr)
                arr[0]=j+dx
                val2=extract.main(exp,arr)
                sum+=(val1+val2)/2*dx
                j=j+dx
        else:
            j=upper
            sum=0.0
            while(j<downer):
                arr[0]=j
                val1=extract.main(exp,arr)
                arr[0]=j-dx
                val2=extract.main(exp,arr)
                sum+=(val1+val2)/2*dx
                j=j-dx
        return sum
    
def CosCoeff(exp,n,p1,p2):
    if(p1==-1*math.pi and p2==math.pi):
        term=integrate(exp+"cos("+str(n)+"*"+"x)",p1,p2)/(p2-p1)
    else:
        term=integrate(exp+"cos("+str(n)+"*"+str(math.pi)+"*"+"x/"+str((p2-p1)/2)+")",-p1,p2)/((p2-p1)/2)
    if(math.fabs(term)<10e-10):
        return 0
    else:
        return term

def SinCoeff(exp,n,p1,p2):
    if(n==0):
        return 0
    if(p1==-1*math.pi and p2==math.pi):
        term=integrate(exp+"sin("+str(n)+"*"+"x)",p1,p2)/((p2-p1)/2)
    else:
        
        term=integrate(exp+"sin("+str(n)+"*"+str(math.pi)+"*"+"x/"+str((p2-p1)/2)+")",-p1,p2)/((p2-p1)/2)
    if(math.fabs(term)<10e-10):
        return 0
    else:
        return term

def FourierCoeff(exp,n,p1,p2):
    real=CosCoeff(exp,math.fabs(n),p1,p2)
    imag=SinCoeff(exp,math.fabs(n),p1,p2)
    if(n<0):
        z=complex(real/2,imag/2)
    else:
        z=complex(real/2,-1*imag/2)
    return z


def discreteFourier(x,n):
    if(len(x)==1):
        return [x[0]]
    else:
        e=[]
        o=[]
        ek=[]
        ok=[]
        for i in range(int(n/2)):
            e.append(x[2*i])
            o.append(x[2*i+1])
        ek=discreteFourier(e,len(e))
        ok=discreteFourier(o,len(o))
        y=[None]*n
        for i in range(int(n/2)):
           y[i]=ek[i]+cmath.rect(1,-1*2*math.pi*i/n)*ok[i]
           y[i+int(n/2)]=ek[i]-cmath.rect(1,-1*2*math.pi*i/n)*ok[i]
        return y


def inverseFourier(x,n):
    if(len(x)==1):
        return [x[0]]
    else:
        e=[]
        o=[]
        ek=[]
        ok=[]
        for i in range(int(n/2)):
            e.append(x[2*i])
            o.append(x[2*i+1])
        ek=inverseFourier(e,len(e))
        ok=inverseFourier(o,len(o))
        y=[None]*n
        for i in range(int(n/2)):
           y[i]=(ek[i]+cmath.rect(1,2*math.pi*i/n)*ok[i])
           y[i+int(n/2)]=(ek[i]-cmath.rect(1,2*math.pi*i/n)*ok[i])
        return y

def inverseVal(x,n):
    y=inverseFourier(x,n)
    try:
        for i in range(n):
           y[i]=y[i]/n
        return y
    except:
        return("input error")
#x=[]
#for i in range(int(math.pow(2,8))):
 #   x.append(i)
#t1=time.time()
#print(discreteFourier(inverseVal([1+0j,2+0j,6788+0j,34+0j],4),4))
#print(time.time()-t1)




    

            
