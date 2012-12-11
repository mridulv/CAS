import math
import extract
import cython
import time
from numpy import matrix
def main(exp,x,y,y1=0,y2=0,y3=0):
    if(not('x' in exp) and not('y' in exp) and not('y\'' in exp) and not('y\'\'' in exp) and not('y\'\'\'' in exp)):
        return float(exp)
    if(exp[0]=='-'):
        exp='0'+exp
    if('(-' in exp):
        exp=exp.replace('(-','(0-')
    temp=[]
    temp=extract.argumentSeparator(exp)
    postfixStr=[]
    postfixStr=extract.convert_infix(temp)
    for i in range(0,len(postfixStr)):
        if(postfixStr[i]=='x'):
            postfixStr[i]=x
        if(postfixStr[i]=='y'):
            postfixStr[i]=y
        if(postfixStr[i]=='y\''):
            postfixStr[i]=y1
        if(postfixStr[i]=='y\'\''):
            postfixStr[i]=y2
        if(postfixStr[i]=='y\'\'\''):
            postfixStr[i]=y3
    finalVal=extract.PostfixEval(postfixStr)
    return finalVal

def solveDiffEqn4(eqn,init,x0,x1):
    begin=x0
    h=(x1-x0)/1000
    array1=[]
    array2=[]
    array3=[]
    array4=[]
    for i in range(1001):
        array1.append(0)
        array2.append(0)
        array3.append(0)
        array4.append(0)
    array1[0]=init[0]
    array2[0]=init[1]
    array3[0]=init[2]
    array4[0]=init[3]
    count=0
    temp=[]
    for i in range(5):
        temp.append(0)
    k1=cython.declare(cython.double)
    k2=cython.declare(cython.double)
    k3=cython.declare(cython.double)
    k4=cython.declare(cython.double)
    while(begin<x1 and count<1000):
        k1=main(eqn,begin,array1[count],array2[count],array3[count],array4[count])
        index=3
        temp[3]=h/2*k1
        while(index>=0):
            temp[index]=h/2*temp[index+1]
            index=index-1
            
        k2=main(eqn,begin+h/2,array1[count]+temp[0]+(h**3/8)*array3[count]+(h**2/4)*array2[count]+h/2*array1[count],array2[count]+temp[1]+((h**2)/4)*array3[count]+h/2*array2[count],array3[count]+temp[2]+h/2*array3[count],array4[count]+temp[3])
        index=3
        temp[3]=h/2*k2
        while(index>=0):
            temp[index]=h/2*temp[index+1]
            index=index-1
            
        k3=main(eqn,begin+h/2,array1[count]+temp[0]+(h**3/8)*array3[count]+(h**2/4)*array2[count]+h/2*array1[count],array2[count]+temp[1]+((h**2)/4)*array3[count]+h/2*array2[count],array3[count]+temp[2]+h/2*array3[count],array4[count]+temp[3])
        index=3
        temp[3]=h*k3
        while(index>=0):
            temp[index]=h*temp[index+1]
            index=index-1
            
        k4=main(eqn,begin+h/2,array1[count]+temp[0]+(h**3)*array3[count]+(h**2)*array2[count]+h*array1[count],array2[count]+temp[1]+((h**2))*array3[count]+h*array2[count],array3[count]+temp[2]+h*array3[count],array4[count]+temp[3])
        
        array4[count+1]=array4[count]+h*(k1+2*k2+2*k3+k4)/6
        array3[count+1]=array3[count]+math.pow(h,2)*(k1+2*k2+2*k3)/10+h*array4[count]
        array2[count+1]=array2[count]+math.pow(h,3)*(k1+2*k2)/18+h*array3[count]
        array1[count+1]=array1[count]+math.pow(h,4)*(k1)/24+h*array2[count]
        count=count+1
        begin+=h
    return array1[1000]

def solveDiffEqn2(eqn,init,x0,x1):
    begin=x0
    h=(x1-x0)/1000
    array1=[]
    array2=[]
    for i in range(1001):
        array1.append(0)
        array2.append(0)
    array1[0]=init[0]
    array2[0]=init[1]
    count=0
    temp=[]
    for i in range(2):
        temp.append(0)
    k1=cython.float
    k2=cython.float
    k3=cython.float
    k4=cython.float
    while(begin<x1 and count<1000):
        k1=main(eqn,begin,array1[count],array2[count])
        index=0
        temp[1]=h/2*k1
        temp[index]=h/2*temp[index+1]
            
        k2=main(eqn,begin+h/2,array1[count]+temp[0]+temp[1],array2[count]+temp[1])
        index=0
        temp[1]=h/2*k2
        temp[index]=h/2*temp[index+1]
            
        k3=main(eqn,begin+h/2,array1[count]+temp[0]+temp[1],array2[count]+temp[1])
        index=0
        temp[1]=h*k3
        temp[index]=h*temp[index+1]
    
            
        k4=main(eqn,begin+h,array1[count]+temp[0]+temp[1],array2[count]+temp[1])
        array2[count+1]=array2[count]+h*(k1+2*k2+2*k3+k4)/6
        array1[count+1]=array1[count]+math.pow(h,2)*(k1+k2+2*k3)/5+h*array2[count]
        count=count+1
        begin+=h
        
    return array1[1000]

def solveDiffEqn3(eqn,init,x0,x1):
    begin=x0
    h=(x1-x0)/1000
    array=[None]*3
    for i in range(3):
        array[i]=[None]*1001
    array[0][0]=init[0]
    array[1][0]=init[1]
    array[2][0]=init[2]
    count=0
    temp=[]
    for i in range(3):
        temp.append(0)
    k1=cython.float
    k2=cython.float
    k3=cython.float
    k4=cython.float
    while(begin<x1 and count<1000):
        k1=main(eqn,begin,array[0][count],array[1][count],array[2][count])
        index=1
        temp[2]=h/2*k1
        while(index>=0):
            temp[index]=h/2*temp[index+1]
            index=index-1
            
        k2=main(eqn,begin+h/2,array[0][count]+temp[0]+h/2*array[1][count]+(h**2/4*array[2][count]),array[1][count]+temp[1]+h/2*array[2][count],array[2][count]+temp[2])
        index=1
        temp[2]=h/2*k2
        while(index>=0):
            temp[index]=h/2*temp[index+1]
            index=index-1
            
        k3=main(eqn,begin+h/2,array[0][count]+temp[0]+h/2*array[1][count]+(h**2/4*array[2][count]),array[1][count]+temp[1]+h/2*array[2][count],array[2][count]+temp[2])     
        temp[2]=h*k3
        while(index>=0):
            temp[index]=h*temp[index+1]
            index=index-1

            
        k4=main(eqn,begin+h,array[0][count]+temp[0]+h*array[1][count]+(h**2*array[2][count]),array[1][count]+temp[1]+h*array[2][count],array[2][count]+temp[2])
        
        array[2][count+1]=array[2][count]+h*(k1+2*k2+2*k3+k4)/6
        array[1][count+1]=array[1][count]+math.pow(h,2)*(k1+2*k2+2*k3)/10+h*array[2][count]
        array[0][count+1]=array[0][count]+math.pow(h,3)*(k1+2*k2)/18+h*array[1][count]
        count=count+1
        begin+=h
    return array[0][1000]

def solveDiffEqn1(eqn,init,x0,x1):
    begin=x0
    h=(x1-x0)/1000
    array1=[]
    for i in range(1001):
        array1.append(0)
    array1[0]=init[0]
    count=0
    k1=cython.float
    k2=cython.float
    k3=cython.float
    k4=cython.float
    while(begin<x1 and count<1000):
        k1=main(eqn,begin,array1[count])
        k2=main(eqn,begin+h/2,array1[count]+h/2*k1)
        k3=main(eqn,begin+h/2,array1[count]+h/2*k2)
        k4=main(eqn,begin+h,array1[count]+h*k3)
        array1[count+1]=array1[count]+(h/6)*(k1+2*k2+2*k3+k4)
        count=count+1
        begin+=h
    return array1[1000]

def MatrixFill(A,i,j,D,I,m):
    if(i==j):
        a=0
        while(a<m):
            b=0
            while(b<m):
                A[i+a][j+b]=D[a][b]
                b=b+1
            a=a+1            
    elif(math.fabs(i-j)==m):
        a=0
        while(a<m):
            b=0
            while(b<m):
                A[i+a][j+b]=I[a][b]
                b=b+1
            a=a+1

def LaplaceEqn(g,boundary,boundary1,pts,pt):
    for i in range(len(pts)):
        pts[i]=int(pts[i])
    #print(pts)
    pt[0]=float(pt[0])
    pt[1]=float(pt[1])
   # print(pt)
    m=int(math.fabs(int(pts[0]/1)))
    n=int(math.fabs(int(pts[1]/1)))
    t1=1
    t2=1
    A=[0]*((m-1)*(n-1))
    for i in range((m-1)*(n-1)):
        A[i]=[0]*((m-1)*(n-1))
    D=[0]*(m-1)
    I=[0]*(m-1)
    for i in range(m-1):
        D[i]=[0]*(m-1)
        I[i]=[0]*(m-1)
        for j in range(m-1):
            if(i==j):
                D[i][j]=4
                I[i][j]=-1
            elif(math.fabs(i-j)==1):
                D[i][j]=-1
    i=0
    while(i<((m-1)*(n-1))):
        j=0
        while(j<((m-1)*(n-1))):
            MatrixFill(A,i,j,D,I,m-1)
            j+=(m-1)
        i+=(m-1)
    val=[]
    if(pts[0]<0):
        t1=-1
    if(pts[1]<0):
        t2=-1
    y_cor=1*t2
    for i in range(n-1):
        x_cor=1*t1
        for j in range(m-1):
            if(math.fabs(x_cor)==1 and math.fabs(y_cor)==1):
                val.append(extract.main(boundary[0],[x_cor,y_cor])+extract.main(boundary[1],[x_cor,y_cor])-extract.main(g,[x_cor,y_cor])*(math.pow(1,2)))
            elif((x_cor)==(pts[0]-1*t1) and (y_cor)==(pts[1]-1*t2)):
                val.append(extract.main(boundary1[0],[x_cor,y_cor])+extract.main(boundary1[1],[x_cor,y_cor])-extract.main(g,[x_cor,y_cor])*(math.pow(1,2)))
            elif((x_cor)==(pts[0]-1*t1) and math.fabs(y_cor)==1):
                val.append(extract.main(boundary1[0],[x_cor,y_cor])+extract.main(boundary[1],[x_cor,y_cor])-extract.main(g,[x_cor,y_cor])*(math.pow(1,2)))
            elif((y_cor)==(pts[1]-1*t2) and math.fabs(x_cor)==1):
                val.append(extract.main(boundary[0],[x_cor,y_cor])+extract.main(boundary1[1],[x_cor,y_cor])-extract.main(g,[x_cor,y_cor])*(math.pow(1,2)))
            elif(math.fabs(x_cor)==1):
                val.append(extract.main(boundary[1],[x_cor,y_cor])-extract.main(g,[x_cor,y_cor])*(math.pow(1,2)))
            elif(math.fabs(y_cor)==1):
                val.append(extract.main(boundary[0],[x_cor,y_cor])-extract.main(g,[x_cor,y_cor])*(math.pow(1,2)))
            elif((x_cor)==(pts[0]-1*t1)):
                val.append(extract.main(boundary1[1],[x_cor,y_cor])-extract.main(g,[x_cor,y_cor])*(math.pow(1,2)))
            elif((y_cor)==(pts[1]-1*t2)):
                val.append(extract.main(boundary1[0],[x_cor,y_cor])-extract.main(g,[x_cor,y_cor])*(math.pow(1,2)))
            else:
                val.append(extract.main(g,[x_cor,y_cor])*(math.pow(1,2))*-1)
            x_cor+=1*t1
        y_cor+=1*t2
    A=matrix(A)
    val=matrix(val)
    u=(A.I)*(val.T)
    u.tolist()
    x1=int(pt[0])
    y1=int(pt[1])
    w1=max(1-math.sqrt((x1-pt[0])**2+(y1-pt[1])**2),0)
    w2=max(1-math.sqrt((x1+t1-pt[0])**2+(y1-pt[1])**2),0)
    w3=max(1-math.sqrt((x1-pt[0])**2+(y1+t2-pt[1])**2),0)
    w4=max(1-math.sqrt((x1+t1-pt[0])**2+(y1+t2-pt[1])**2),0)
    if(x1!=0 and y1!=0):
        u1=u[math.fabs(x1)-1+(m-1)*(math.fabs(y1)-1)]
    else:
        if(x1==0):
            u1=extract.main(boundary[1],[x1,y1])
        elif(y1==0):
            u1=extract.main(boundary[0],[x1,y1])
    if(y1!=0 and x1!=pts[0]-t1):
        u2=u[math.fabs(x1)+(m-1)*(math.fabs(y1)-1)]
    else:
        if(y1==0):
            u2=extract.main(boundary[0],[x1,y1])
        elif(x1==pts[0]-t1):
            u2=extract.main(boundary1[1],[x1,y1])
    if(x1!=0 and y1!=pts[1]-t2):
        u3=u[math.fabs(x1)-1+(m-1)*(math.fabs(y1))]
    else:
        if(x1==0):
            u3=extract.main(boundary[1],[x1,y1])
        elif(y1==pts[1]-t2):
            u3=extract.main(boundary1[1],[x1,y1])
    if(x1!=pts[0]-t1 and y1!=pts[1]-t2):
       u4=u[math.fabs(x1)+(m-1)*(math.fabs(y1))]
    else:
       if(x1==pts[0]-t1):
            u4=extract.main(boundary1[1],[x1,y1])
       elif(y1==pts[1]-t2):
            u4=extract.main(boundary1[1],[x1,y1]) 
    u_final=(w1*u1+w2*u2+w3*u3+w4*u4)/(w1+w2+w3+w4)
    return(u_final)

#print(LaplaceEqn('0',['0','0'],['10x','10y'],['10','10'],['9.5','1.87']))

            


    
    
   




        
        
           
        
    



