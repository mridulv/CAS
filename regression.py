
import math
from Polynomial_final import *
from extract import *
from numpy import *

obj=Polynomial()
def LeastSquare(deg,x,y):
    if(deg<=2):
        polyn=["1"]
        for i in range(deg):
            polyn.append("x^"+str(i+1))
    else:
        polyn=OrthoNormalPolynomial(deg+1)
    print(polyn)
    A=[[None]*(deg+1) for i in range(len(x))]
    B=[None]*len(y)
    for i in range(len(x)):
        for j in range(deg+1):
            A[i][j]=main(polyn[j],[x[i]])
        B[i]=y[i]
    A=matrix(A)
    B=matrix(B)
    try:
        C=(A.T)*A
        D=(C.I)*(A.T*B.T)
        D1=array(D)
        e='0'
        for i in range(deg+1):
           e=obj.addPolynomial(e,obj.MultiplyPolynomial(polyn[i],str(D1[i][0])))
        return(e)
    except:
        return("No curve possible for these data points.Try again with other points")
    
def ExponentialCurve(x,y):
    for i in range(len(x)):
        y[i]=math.log(y[i],math.e)
    A=[[None]*2 for i in range(len(x))]
    B=[None]*(len(x))
    for i in range(len(x)):
        A[i][0]=1
        A[i][1]=x[i]
        B[i]=y[i]
    A=matrix(A)
    B=matrix(B)
    try:
        C=(A.T)*A
        D=(C.I)*(A.T*B.T)
        D1=array(D)
        D1[0][0]=math.exp(D1[0][0])
        e=''
        e=str(D1[0][0])+"exp("+str(D1[1][0])+"x)"
        return e
    except:
        return("No curve possible for these data points.Try again with other points")

def LogarithmicCurve(x,y):
    for i in range(len(x)):
        x[i]=math.log(x[i],math.e)
    A=[[None]*2 for i in range(len(x))]
    B=[None]*(len(x))
    for i in range(len(x)):
        A[i][0]=1
        A[i][1]=x[i]
        B[i]=y[i]
    A=matrix(A)
    B=matrix(B)
    try:
        C=(A.T)*A
        D=(C.I)*(A.T*B.T)
        D1=array(D)
        D1[0][0]=math.exp(D1[0][0]/D1[1][0])
        e=''
        e=str(D1[1][0])+"log("+str(D1[0][0])+"x)"
        return e
    except:
        return("No curve possible for these data points.Try again with other points")

def PlaneFit(x,y,z):
    A=[[None]*3 for i in range(len(x))]
    B=[None]*(len(x))
    for i in range(len(x)):
        A[i][0]=1
        A[i][1]=x[i]
        A[i][2]=y[i]
        B[i]=z[i]
    A=matrix(A)
    B=matrix(B)
    try:
        C=(A.T)*A
        D=(C.I)*(A.T*B.T)
        D1=array(D)
        e=''
        e=str(D1[0][0])+"+"+str(D1[1][0])+"x+"+str(D1[2][0])+"y-z=0"
        return e
    except:
        return("No curve possible for these data points.Try again with other points")
    
def SpearsmanCoff(x,y):
    xlen=len(x)
    index_x=numpy.array(x).argsort()
    pos_x=[]
    index_x=list(index_x)
    index_y=numpy.array(y).argsort()
    pos_y=[]
    index_y=list(index_y)
    for i in range(len(x)):
        pos_x.append(index_x.index(i))
        pos_y.append(index_y.index(i))
    i=1
    while(i<len(x)):
        if(x[index_x[i]]==x[index_x[i-1]]):
            s=i-1
            j=i-1
            while(i<xlen and x[index_x[i]]==x[index_x[i-1]]):
                s=s+i
                i=i+1
            s/=(i-j)
            for k in range(j,i):
                pos_x[index_x[k]]=s
        else:
            i=i+1
    i=1
    while(i<len(x)):
        if(y[index_y[i]]==y[index_y[i-1]]):
            s=i-1
            j=i-1
            while(i<xlen and y[index_y[i]]==y[index_y[i-1]]):
                s=s+i
                i=i+1
            s/=(i-j)
            for k in range(j,i):
                pos_y[index_y[k]]=s
        else:
            i=i+1
    sx=sum(pos_x)
    sy=sum(pos_y)
    mean_x=sx/len(pos_x)
    mean_y=sy/len(pos_y)
    s1=s2=s3=0
    for i in range(xlen):
        s1+=(pos_x[i]-mean_x)*(pos_y[i]-mean_y)
        s2+=math.pow(pos_x[i]-mean_x,2)
        s3+=math.pow(pos_y[i]-mean_y,2)
    #print("laal",s1/(math.sqrt(s2*s3)))
    return s1/(math.sqrt(s2*s3))

def Pearson(x,y):
    x_i=0
    y_i=0
    xy_i=0
    for i in range(len(x)):
       x_i+=x[i]
       y_i+=y[i]
       xy_i+=x[i]*y[i]
    x_i=x_i/len(x)
    y_i=y_i/len(y)
    xy_i=xy_i/len(x)
    sd_x=0
    sd_y=0
    for i in range(len(x)):
        sd_x+=x[i]**2
        sd_y+=y[i]**2
    sd_x=math.sqrt(sd_x/len(x)-x_i**2)
    sd_y=math.sqrt(sd_y/len(y)-y_i**2)
    cov_xy=xy_i-x_i*y_i
    pearson=cov_xy/(sd_x*sd_y)
    return pearson

def MergeSort(x,count):
    if(len(x)==1):
        return x
    else:
        y=MergeSort(x[0:int(len(x)/2)],count)
        z=MergeSort(x[int(len(x)/2):len(x)],count)
        i=j=k=0
        while(i<len(y) or j<len(z)):
            if(i<len(y) and j<len(z)):
                if(y[i]<z[j]):
                    x[k]=(y[i])
                    if(k>i):
                        count.append(k-i)
                    i=i+1
                else:
                    x[k]=(z[j])
                    j=j+1
            elif(i>=len(y)):
                x[k]=z[j]
                j=j+1
            else:
                x[k]=(y[i])
                count.append(k-i)
                i=i+1
            k=k+1
        return x

def tau(arr):
    temp=[]
    count=[]
    merge_y=[]
    for i in range(int(len(arr))):
        temp.append(arr[i][0])
    index_x=numpy.array(temp).argsort()
    merge_x=MergeSort(temp,count)
    for i in range(int(len(arr))):
        merge_y.append(arr[index_x[i]][1])
    for i in range(int(len(arr)-1)):
        if(i<len(arr) and merge_x[i]==merge_x[i+1]):
            j=i
            while(i<len(arr) and merge_x[i]==merge_x[i+1]):
                i+=1
            count=[]
            merge_y[j:i+1]=MergeSort(merge_y[j:i+1],count)
    count=[]
    MergeSort(merge_y,count)
    s1=sum(count)
    temp=[]
    merge_x=[]
    for i in range(int(len(arr))):
        temp.append(arr[i][1])
    count=[]
    index_y=numpy.array(temp).argsort()
    merge_y=MergeSort(temp,count)
    for i in range(int(len(arr))):
        merge_x.append(arr[index_y[i]][0])
    for i in range(int(len(arr)-1)):
        if(i<len(arr) and merge_y[i]==merge_y[i+1]):
            j=i
            while(i<len(arr) and merge_y[i]==merge_y[i+1]):
                i+=1
            count=[]
            merge_x[j:i+1]=MergeSort(merge_x[j:i+1],count)
    count=[]
    MergeSort(merge_x,count)
    s2=sum(count)
    count=[]
    s=(s1+s2)/2
    tau=1-4*s/(len(arr)*(len(arr)-1))
    return tau

def SplineInterpolation(arr):
    b=[]
    a=[None]*(len(arr))
    for i in range(len(arr)):
        a[i]=[0]*(len(arr))
        if(i==0):
            b.append(3*(arr[1][1]-arr[0][1])/(math.pow(arr[1][0]-arr[0][0],2)))
            a[i][0]=2/(arr[1][0]-arr[0][0])
            a[i][1]=1/(arr[1][0]-arr[0][0])
        elif(i==len(arr)-1):
            b.append(3*(arr[i][1]-arr[i-1][1])/(math.pow(arr[i][0]-arr[i-1][0],2)))
            a[i][len(arr)-2]=1/(arr[i][0]-arr[i-1][0])
            a[i][len(arr)-1]=2/(arr[i][0]-arr[i-1][0])     
        else:
            b.append(3*((arr[i][1]-arr[i-1][1])/(math.pow(arr[i][0]-arr[i-1][0],2))+((arr[i+1][1]-arr[i][1])/(math.pow(arr[i+1][0]-arr[i][0],2)))))
            a[i][i-1]=1/(arr[i][0]-arr[i-1][0])
            a[i][i]=2*(1/(arr[i][0]-arr[i-1][0])+1/(arr[i+1][0]-arr[i][0]))
            a[i][i+1]=1/(arr[i+1][0]-arr[i][0])
    a=matrix(a)
    b=matrix(b)
    try:
        k=(a.I)*(b.T)
        k=k.tolist()
        A=[]
        B=[]
        for i in range(1,len(k)):
            A.append(k[i-1][0]*(arr[i][0]-arr[i-1][0])-(arr[i][1]-arr[i-1][1]))
            B.append(-1*k[i][0]*(arr[i][0]-arr[i-1][0])+(arr[i][1]-arr[i-1][1]))
        q=[]
        for i in range(1,len(arr)):
            t1=obj.MultiplyPolynomial(str(1/(arr[i][0]-arr[i-1][0])),str(arr[i][0])+"-x")
            if(arr[i-1][0]>0):
                t2=obj.MultiplyPolynomial("x-"+str(arr[i-1][0]),str(1/(arr[i][0]-arr[i-1][0])))
            else:
                t2=obj.MultiplyPolynomial("x+"+str(math.fabs(arr[i-1][0])),str(1/(arr[i][0]-arr[i-1][0])))
            t3=obj.MultiplyPolynomial(t1,t2)
            t4=obj.addPolynomial(obj.MultiplyPolynomial(str(A[i-1]),t1),obj.MultiplyPolynomial(str(B[i-1]),t2))
            t5=obj.MultiplyPolynomial(t3,t4)
            t6=obj.addPolynomial(obj.MultiplyPolynomial(str(arr[i-1][1]),t1),obj.MultiplyPolynomial(str(arr[i][1]),t2))
            q.append(obj.addPolynomial(t5,t6))
        return q
    except:
        return("Unexpected Input")





        

                 
        
            
            
    
    

