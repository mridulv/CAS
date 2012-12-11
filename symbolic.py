import extract
import math
import cython
import random
import numpy
from optimize import *
import scipy
import time
import extract
def differentiation(exp,var):
    if(not(var in exp)):
        return ["0"]
    diff=[]
    if(extract.isOperand(exp[len(exp)-1])==1):
        if(exp[len(exp)-1]==var):
            diff.append("1")
            return diff
        else:
            diff.append("0")
            return diff
    if(extract.isTrncdDef(exp[len(exp)-1])):
        op=exp[len(exp)-1]
        u=exp[0:len(exp)-1]
        du=differentiation(u,var)
        if(op=='sin'):
            diff=u+['cos']+du+['*']
            return diff
        if(op=='cos'):
            diff=['0']+u+['sin']+du+['*']+['-']
            return diff
        if(op=='exp'):
            diff=u+['exp']+du+['*']
            return diff
        if(op=='log'):
            diff=['1']+u+['/']+du+["*"]
            return diff
        if(op=='tan'):
            diff=u+['sec','2','^']+du+['*']
            return diff
        if(op=='cot'):
            diff=['0']+u+['cosec','2','^']+du+['*','-']
            return diff
        if(op=='sec'):
            diff=u+['sec']+u+['tan','*']+du+['*']
            return diff
        if(op=='cosec'):
            diff=['0']+u+['cosec']+u+['cot','*']+du+['*','-']
            return diff
        if(op=='sinh'):
            diff=u+['cosh']+du+['*']
            return diff
        if(op=='cosh'):
            diff=u+['sinh']+du+['*']
            return diff
        if(op=='tanh'):
            diff=['1']+u+['tan','2','^','-']+du+['*']
            return diff
        if(op=='asin'):
            diff=['1','1']+u+['2','^','-','0.5','^','/']+du+['*']
            return diff
        if(op=='acos'):
            diff=['0','1','1']+u+['2','^','-','0.5','^','/']+du+['*','-']
            return diff
        if(op=='atan'):
            diff=['1','1']+u+['2','^','+','/']+du+['*']
            return diff
        if(op=='mod'):
            diff=u+u+['mod','/']+du+['*']
            return diff
        
    k=0
    i=len(exp)-2
    while(k>=0):
        if(extract.isOperand(exp[i])==1):
           k=k-1
        elif(extract.isOperator(exp[i])==1):
           k=k+1
        i=i-1
    op=exp[len(exp)-1]
    u=exp[0:i+1]
    v=exp[i+1:len(exp)-1]
    du=differentiation(u,var)
    dv=differentiation(v,var)
    if(op=='+'):
        if(du==['0']):
            diff=(dv)
        elif(dv==["0"]):
            diff=(du)
        else:
            diff=(du+dv+['+'])
        return diff
    elif(op=='-'):
        if(du==["0"]):
            diff=(['0']+dv+["-"])
        elif(dv==["0"]):
            diff=(du)
        else:
            diff=(du+dv+["-"])
        return diff
    elif(op=='*'):
        if(du==["0"]):
            diff=(u+dv+["*"])
        elif(dv==["0"]):
            diff=(v+du+["*"])
        else:
            diff=u+dv+["*"]+v+du+["*"]+["+"]
        return diff
    elif(op=='/'):
        if(dv==["0"]):
            diff=(du+v+["/"])
        elif(du=="0"):
            diff=(["0"]+u+["-"]+dv+["*"]+v+["2","^","/"])
        else:
            diff=(v+du+["*"]+u+dv+["*","-"]+v+["2","^","/"])
        return diff
    else:
        if(not(var in v)):
            vs=[]
            for i in v:
                vs.append(i)
            try:
                vs=eval(extract.post_infix(vs))
                if(vs>0):
                    diff=[str(vs)]+u+[str(vs-1)]+['^']+['*']+du+['*']
                else:
                    diff=['0']+[str(vs*(-1))]+['-']+u+['0']+[str((vs-1)*-1)]+['-']+['^']+['*']+du+['*']
                return diff
            except:
                diff=v+u+v+['1']+['-']+['^']+['*']
                return diff
        elif(not(var in u)):
            diff=u+v+['^']+u+['log']+dv+['*','*']
            return diff
        else:
            diff=u+v+['^']+v+u+['/']+du+['*']+dv+u+['log','*','+','/']
            return diff

def CallDiff(exp,var):
    res=extract.argumentSeparator(exp)
    res=differentiation(extract.convert_infix(res),var)
    res= extract.post_infix(res)
    return res
    
var_list=['x','y','z','u','v','w']
def Laplacian(exp):
    der1=[]
    der2=[]
    for i in range(len(var_list)):
        der1.append(CallDiff(exp,var_list[i]))
        der2.append(CallDiff(der1[i],var_list[i]))
     
    return der2

def dirDeriv(exp,point,vector):
    dim=len(vector)
    dird=[]
    for i in range(dim):
        dird.append(CallDiff(exp,var_list[i]))
    comp=[]
    try:
        for i in range(dim):
            comp.append(extract.main(dird[i],point)*vector[i])
        return comp
    except:
        return("function not derivable")

def dimcheck(exp):
    if 'w' in exp:
        return 6
    if 'v' in exp:
        return 5
    if 'u' in exp:
        return 4
    if 'z' in exp:
        return 3
    if 'y' in exp:
        return 2
    if 'x' in exp:
        return 1
    
def Factorial(x):
    fact=cython.declare(cython.longdouble,1)
    i=1
    while(i<=x):
        fact*=i
        i=i+1
    return fact

def funcType(exp,upper):
    flag=0
    for i in range(10):
        t1=random.random()*(upper)-upper
        val1=extract.main(exp,[t1])
        val2=extract.main(exp,[-1*t1])
        if(val1==val2):
            flag+=1
        elif(val1==-1*val2):
            flag-=1
        else:
            flag=0
    return flag


def integrate(exp,downer,upper):
    try:
        if(downer=='-inf'):
            downer=-300
        if(upper=='inf'):
            upper=300
        if(not('x' in exp)):
            return(float(exp)*(upper-downer))
        if(math.fabs(downer)==math.fabs(upper)):
            flag=funcType(exp,upper)
            if(flag==10):
               exp="2*("+exp+")"
               downer=0
            if(flag==-10):
               return 0
        dx=(upper-downer)/1000
        if(math.fabs(dx)<1):
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
        else:
                down_lim=[downer]
                up_lim=[downer+(upper-downer)/10]
                sum=0
                for i in range(10):
                    sum+=integrate(exp,down_lim[i],up_lim[i])
                    down_lim.append(up_lim[i])
                    up_lim.append(up_lim[i]+(upper-downer)/10)
                return sum
    except:
        return("unexpected input")
                
           
def differentiate(exp,x,order):
    arr=[x]
    i=1
    for i in range(1,order+1):
        if(not('x' in exp)):
            return 0
        exp=CallDiff(exp,'x')
    try:
        der=extract.main(exp,arr)
        return der
    except:
        return("function not derivable")

def Max(exp,dim,low_bound,up_bound):
    gr=(numpy.array(up_bound))>=(numpy.array(low_bound))
    if(False in gr):
        for i in range((len(low_bound))):
            if(gr[i]==False):
                (up_bound[i],low_bound[i])=(low_bound[i],up_bound[i])
    exp="0-("+exp+")"
    maxm=-1*optimize_min(exp,dim,low_bound,up_bound)
    for i in range(200):
        max=-1*optimize_min(exp,dim,low_bound,up_bound)
        if(max>maxm):
            maxm=max
    return maxm
        
def Min(exp,dim,low_bound,up_bound):
    gr=(numpy.array(up_bound))>=(numpy.array(low_bound))
    if(False in gr):
        for i in range((len(low_bound))):
            if(gr[i]==False):
                (up_bound[i],low_bound[i])=(low_bound[i],up_bound[i])
    minm=optimize_min(exp,dim,low_bound,up_bound)
    for i in range(200):
        min=optimize_min(exp,dim,low_bound,up_bound)
        if(min<minm):
            minm=min
    return minm

def multiDimensionInteg(exp,dim,down,up):
    minarr=[None]*dim
    maxarr=[None]*dim
    res=0.0
    pro=1.0
    j=0
    flag_down=[]
    flag_up=[]
    while(j<dim):
        flag_down.append(0)
        flag_up.append(0)
        k=j-1
        while(k>=0):
            if(var_list[k] in str(up[j])):
                flag_up[j]=1
            if(var_list[k] in str(down[j])):
                flag_down[j]=1
            k=k-1
        if(flag_up[j]==0 and flag_down[j]==0):
            minarr[j],maxarr[j]=float(down[j]),float(up[j])
        elif(flag_up[j]==1 and flag_down[j]==0):
            temp1=(Max(up[j],j,minarr[0:j],maxarr[0:j]))
            temp2=(Min(up[j],j,minarr[0:j],maxarr[0:j]))
            temp3=float(down[j])
            if(temp1>=temp3):
                maxarr[j]=temp1
            else:
                maxarr[j]=temp3
            if(temp2<=temp3):
                minarr[j]=temp2
            else:
                minarr[j]=temp3
        elif(flag_up[j]==0 and flag_down[j]==1):
            temp1=(Max(down[j],j,minarr[0:j],maxarr[0:j]))
            temp2=(Min(down[j],j,minarr[0:j],maxarr[0:j]))
            temp3=float(up[j])
            if(temp1>=temp3):
                maxarr[j]=temp1
            else:
                maxarr[j]=temp3
            if(temp2<=temp3):
                minarr[j]=temp2
            else:
                minarr[j]=temp3         
        else:
            temp1=(Max(up[j],j,minarr[0:j],maxarr[0:j]))
            temp2=(Min(up[j],j,minarr[0:j],maxarr[0:j]))
            temp3=(Max(down[j],j,minarr[0:j],maxarr[0:j]))
            temp4=(Min(down[j],j,minarr[0:j],maxarr[0:j]))
            if(temp1>=temp3):
                maxarr[j]=temp1
            else:
                maxarr[j]=temp3
            if(temp2<=temp4):
                minarr[j]=temp2
            else:
                minarr[j]=temp4
        j=j+1
    if(minarr[0]>maxarr[0]):
        minarr[0],maxarr[0]=maxarr[0],minarr[0]
    try:
        
        for i in range(1000):
            arr=[]
            j=0
            while(j<dim):
                arr.append((maxarr[j]-minarr[j])*random.random()+minarr[j])
                j=j+1
            f1=extract.main(exp,arr)
            flag=1
            for k in range(dim):
                temp1=extract.main(down[k],arr[0:k])
                temp2=extract.main(up[k],arr[0:k])
                if(not((arr[k]<temp1 and arr[k]>temp2) or (arr[k]>temp1 and arr[k]<temp2))):
                    flag=0
                if(temp1>temp2):
                    flag=-1*flag
            
            res+=f1*flag
        res/=1000
        for i in range(dim):
            res*=(maxarr[i]-minarr[i])
        return res
    except:
        return("unexpected input")

def EqnSolver(exp,x0,x1):
    count=0
    try:
        while((math.fabs(x1-x0))>0.01  and count<100):
            func1=extract.main(exp,[x1])
            func0=extract.main(exp,[x0])
            if(math.fabs(func1)<0.09 and math.fabs(func0)<0.09):
                break
            x2=x1-func1*(x1-x0)/(func1-func0)
            x0,x1=x1,x2
            count=count+1
        if(count==100):
             return("please try again with better root approximation.Perhaps no roots exist")
        if(math.fabs(x1-x0)<0.1):
            if(math.fabs(func1)<0.09 and math.fabs(func0)<0.09):
                 return x1
            else:
                 return("high probability that roots don't exist")
        else:
            return("two roots were found"+str(x0)+","+str(x1))
    except:
        return("method failed.Please try again with another approximation")

def isMonotone(exp,a,b):
    begin=min(a,b)
    end=max(a,b)
    arr=[]
    interval=(end-begin)/1000
    while(begin<=end):
        arr.append(extract.main(exp,[begin]))
        begin+=interval
    arr.sort()
    if(math.fabs(arr[0]-extract.main(exp,[begin]))<0.01 and math.fabs(arr[len(arr)-1]-extract.main(exp,[end])<0.01)):
       return True
    return False


def roots_interval(exp,a,b):
    roots=[]
    h=(b-a)/1000
    try:
        while(a<=b):
            f1=extract.main(exp,[a])
            f2=extract.main(exp,[a+h])
            if(f1*f2<=0 and (f1*f2)>-10):
                roots.append(a+h/2)
            else:
                if(math.fabs(f1)<0.01):
                   roots.append(a)
            a=a+h
        actual=[]
        if(len(roots)!=0):
            actual.append(roots[0])
        i=1
        count=0
        while(i<len(roots)):
            if(math.fabs(roots[i]-roots[i-1])>0.1):
               actual.append(roots[i])
               count=count+1
               i=i+1
            else:
               j=i
               sum=0
               while(i<len(roots) and math.fabs(roots[i]-roots[i-1])<0.1):
                   sum+=roots[i]
                   i=i+1
               actual[count]=(actual[count]+sum)/(i-j+1)
        return actual
    except:
        return("unexpected value experienced.Try again with a different interval")
    

#print(extract.convert_infix(extract.argumentSeparator("mod(cos(acos(log(1/((0-x+x^2sin(yz)))))))")))
#print(dirDeriv('x^2+y^3z^2',[1,0,0],[5,8,4]))
#print(Laplacian("sin(x)y^(x-3x^2)+log(mod(cosec(x)))"))
#print(integrate("acos(x)log(mod(x))",0.9,-0.9))
#print(roots_interval("-(x+8)",-15,5))
#print(multiDimensionInteg("x",3,['-1','x','y'],['0','x^2','1-y^3']))
#print(Min("x(y)",2,[0,6],[1,9]))
