import extract
import numpy
import random
import math
import time
import cython
def optimize_min(exp,dim,arrmin,arrmax):
    flag=-1
    count=0
    while(count<50):
        count=count+1
        if(flag==0 or flag==-1):
            points=[]*(dim+1)
            values=[]
            for i in range(dim+1):
                points.append([0]*(dim))
                temp=[]*(dim)
                for j in range(dim):
                    temp.append(arrmin[j]+(arrmax[j]-arrmin[j])*random.random())
                points[i]=temp
                values.append(extract.main(exp,points[i]))
                points[i]=numpy.array(points[i])
            values=numpy.array(values)
        index=values.argsort()
        temp=points
        for i in range(dim+1):
            points[i]=temp[index[i]]
        values.sort()
        if(math.fabs((values[dim]-values[0])/values[0])<0.01):
            break
        if(True in (points[dim]-points[0])<numpy.array([0.05]*(dim)) and True in (points[dim]-points[0])>numpy.array([-0.05]*(dim))):
            break
        x0=numpy.array([0]*dim)
        for i in range(dim):
            x0=x0+points[dim]
        x0=x0/dim
        xr=numpy.array([0]*(dim))
        xr=2*x0-points[dim]
        if(extract.main(exp,xr)<values[dim] and extract.main(exp,xr)>=values[0]):
            gr=xr>=numpy.array(arrmin)
            sm=xr<=numpy.array(arrmax)
            if(False in gr or False in sm):
                flag=0
                continue
            points[dim]=xr
            values[dim]=extract.main(exp,xr)
            flag=1
            continue
        elif(extract.main(exp,xr)<values[0]):
            xe=2*xr-x0
            gr=xr>=numpy.array(arrmin)
            sm=xr<=numpy.array(arrmax)
            if(False in gr or False in sm):
                flag=0
                continue
            if(extract.main(exp,xe)<extract.main(exp,xr)):
                points[dim]=xe
                values[dim]=extract.main(exp,xe)
                flag=1
                continue
            else:
                points[dim]=xr
                values[dim]=extract.main(exp,xr)
                flag=1
                continue
        else:
            xc=0.5*xr+0.5*x0
            gr=xr>=numpy.array(arrmin)
            sm=xr<=numpy.array(arrmax)
            if(False in gr or False in sm):
                flag=0
                continue
            if(extract.main(exp,xc)<extract.main(exp,xr)):
                points[dim]=xc
                values[dim]=extract.main(exp,xc)
                flag=1
                continue
            elif(extract.main(exp,xr)>values[dim]):
                xc=0.5*values[dim]+0.5*x0
                if(extract.main(exp,xc)<values[dim]):
                    points[dim]=xc
                    values[dim]=extract.main(exp,xc)
                    flag=1
                    continue
                else:
                    for i in range(1,dim+1):
                        points[i]=0.5*points[0]+0.5*points[i]
                        values[i]=extract.main(exp,points[i])
                        flag=1
    if(math.fabs((values[dim]-values[0])/values[0])<0.01):
        return values[0]
    if(True in (points[dim]-points[0])<([0.05]*(dim)) and True in (points[dim]-points[0])>([-0.05]*(dim))):
        return min(values)
    return min(values)


        
    
