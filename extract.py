import math
import random
import cython
from decimal import *
def push_stack(stackArr,ele):
    stackArr.append(ele)

def pop_stack(stackArr):
    return stackArr.pop()

def isTrncd(val):
    if(val=='s' or val =='c' or val =='t' or val=='l' or val=='e' or val=='m' or val=='a'):
        return 1
    return 0

def isTrncdDef(val):
    if(val=="sin" or val =="cos" or val=="cosec" or val=="sec" or val=="tan" or val=="cot" or val=="log" or val=="exp"  or val=='mod' or val=='asin' or val=='acos' or val=='atan' or val=='sinh' or val =='cosh' or val=='tanh'):
        return 1
    return 0

def isOperand(val):
    if(((not(isOperator(val)) and not(isTrncdDef(val))) and (val != "(") and (val != ")")) and not(isTrncd(val))):
        return 1
    return 0

def isOperator(val):
    if(val == "+" or val == "-" or val == "*" or val == "/" or val == "^"):
        return 1
    return 0

def topStack(stackArr):
    return(stackArr[len(stackArr)-1])

def isEmpty(stackArr):
    if(len(stackArr) == 0):
        return 1
    return 0

def precedence(val):
    if(val == "^"):
        return 5
    elif(val=="/" or val=="*"):
        return 4
    elif(val=="+" or val=="-"):
        return 3
    elif(val=="("):
        return 2
    elif(val==")"):
        return 1
    else:
        return 6
    
def convert_infix(infixStr):
    postfixStr = []
    stackArr = []
    postfixPtr = 0
    tempStr = infixStr
    infixStr = []
    infixStr = strToTokens(tempStr)
    for x in infixStr:
        if(isOperand(x)):
            postfixStr.append(x)
            postfixPtr = postfixPtr+1
        if(isOperator(x) or isTrncdDef(x)):
            if(not(isTrncdDef(x))):
                while((not(isEmpty(stackArr))) and (precedence(x) <= precedence(topStack(stackArr)))):
                    postfixStr.append(topStack(stackArr))
                    pop_stack(stackArr)
                    postfixPtr = postfixPtr+1
            else:
                while((not(isEmpty(stackArr))) and (precedence(x) < precedence(topStack(stackArr)))):
                    postfixStr.append(topStack(stackArr))
                    pop_stack(stackArr)
                    postfixPtr = postfixPtr+1
            push_stack(stackArr,x)
        if(x == "("):
                push_stack(stackArr,x)                
        if(x == ")"):
            while(topStack(stackArr) != "("):
                postfixStr.append(pop_stack(stackArr))
                postfixPtr = postfixPtr+1
            pop_stack(stackArr)
            
    while(not(isEmpty(stackArr))):
        if(topStack(stackArr) == "("):
            pop_stack(stackArr)
        else:
            postfixStr.append(pop_stack(stackArr))

    return(postfixStr)


def strToTokens(str):
    strArr = []
    strArr = str
    tempStr = ''	
    tokens = []
    count = 0
    for x in strArr:
        count = count+1
        if(isOperand(x) or isTrncd(x)):
            tempStr += x
        if(isOperator(x) or x == ")" or x == "("):
            if(tempStr != ""):
                tokens.append(tempStr)
            tempStr = ''
            tokens.append(x) 
        if(count == len(strArr)):
            if(tempStr != ''):
                tokens.append(tempStr)
    return(tokens)

def postfixTrnc(num,sym):
    num=float(num)
    if(sym=="sin"):
        return math.sin(num)
    if(sym=="cos"):
        return math.cos(num)
    if(sym=="tan"):
        return math.tan(num)
    if(sym=="cot"):
        return 1/(math.tan(num))
    if(sym=="cosec"):
        return 1/(math.sin(num))
    if(sym=="sec"):
        return 1/(math.cos(num))
    if(sym=="log"):
        return math.log(num,math.e)
    if(sym=="exp"):
        return math.e**num
    if(sym=='mod'):
        return math.fabs(num)
    if(sym=='asin'):
        return math.asin(num)
    if(sym=='acos'):
        return math.acos(num)
    if(sym=='atan'):
        return math.atan(num)
    if(sym=='sinh'):
        return math.sinh(num)
    if(sym=='cosh'):
        return math.cosh(num)
    if(sym=='tanh'):
        return math.tanh(num)
    
def PostfixSubEval(num1,num2,sym):
    num1,num2 = float(num1),float(num2)
    if(sym == "+"):
        returnVal = float(num1 + num2)
    if(sym == "-"):
        returnVal = float(num1 - num2)
    if(sym == "*"):
        returnVal = float(num1 * num2)
    if(sym == "/"):
        if(num2==0):
            return num1*(10e+12)
        else:
            returnVal = num1/num2
    if(sym == "^"):
        try:
            returnVal= pow(num1,num2)
        except:
            returnVal=10e+12
    return returnVal

def PostfixEval(postfixStr):
    temp = postfixStr
    postfixStr = []
    postfixStr = temp
    stackArr = []
    for x in postfixStr:
        if(isOperand(x)):
            push_stack(stackArr,x)
        elif(isOperator(x)):
            temp = topStack(stackArr)
            pop_stack(stackArr)
            pushVal = PostfixSubEval(topStack(stackArr),temp,x)
            pop_stack(stackArr)
            push_stack(stackArr,pushVal)
        else:
            pushVal=postfixTrnc(topStack(stackArr),x)
            pop_stack(stackArr)
            push_stack(stackArr,pushVal)
    return(topStack(stackArr))

def argumentSeparator(exp):
    variables=['u','v','w','x','y','y\'','y\'\'','y\'\'\'','z','s','c','l','e','t','m','a']
    if(exp[0]=='-'):
        exp='0'+exp

    if('(-' in exp):
        exp=exp.replace('(-','(0-')
    temp=''
    for i in range(0,len(exp)-1):
        if(((exp[i]>='0' and exp[i]<='9') or exp[i]==')') and ((exp[i+1] in variables) or exp[i+1]=='(')):
            temp+=exp[i]+'*'
        elif((exp[i] in variables and exp[i+1] in variables)):
            if(exp[i]=='a'):
                temp+=exp[i]
            elif((exp[i]=='e' and exp[i+1]=='x') or (exp[i]=='s' and exp[i+1]=='e') or (exp[i]=='e' and exp[i+1]=='c') or (exp[i]=='t' and exp[i+1]=='a')):
                temp+=exp[i]
            else:
                temp+=exp[i]+"*"
        elif(exp[i]=='\'' and exp[i+1] in variables):
            temp+=exp[i]+'*'
        elif(exp[i] in variables and (exp[i+1]=="(" and not(exp[i-1].isalpha()))):
            temp+=exp[i]+"*"
        else:
            temp+=exp[i]
    temp+=exp[len(exp)-1]
    final=''
    for i in range(0,len(temp)-1):
        if((temp[i]==')') and (temp[i+1] in variables or (temp[i+1]>='0' and temp[i+1]<='9'))):
           final+=temp[i]+"*"
        else:
           final+=temp[i]
    final+=temp[len(temp)-1]
    return final
  
def main(exp,arr):
    if(not('x' in exp) and not('y' in exp) and not('z' in exp) and not('u' in exp) and not('v' in exp) and not('w' in exp)):
        return eval(exp)
    if(exp[0]=='-'):
        exp='0'+exp
    if('(-' in exp):
        exp=exp.replace('(-','(0-')
    temp=[]
    temp=argumentSeparator(exp)
    postfixStr=[]
    postfixStr=convert_infix(temp)
    for i in range(0,len(postfixStr)):
        if(postfixStr[i] =='x'):
            postfixStr[i]=arr[0]
        if(postfixStr[i]=='y'):
            postfixStr[i]=arr[1]
        if(postfixStr[i]=='z'):
            postfixStr[i]=arr[2]
        if(postfixStr[i]=='u'):
            postfixStr[i]=arr[3]
        if(postfixStr[i]=='v'):
            postfixStr[i]=arr[4]
        if(postfixStr[i]=='w'):
            postfixStr[i]=arr[5]
    try:
        finalVal=PostfixEval(postfixStr)
        return finalVal
    except:
        return("domain error encountered")

        
def post_infix(postfixStr):
    stackArr = []
    tempStr = postfixStr
    postfixStr = []
    postfixStr = tempStr
    for x in postfixStr:
        flag=0
        if(isOperand(x)):
            push_stack(stackArr,x)
        elif(isOperator(x)):
            temp = topStack(stackArr)
            pop_stack(stackArr)
            if(x=='+'):
                if((temp[0]=='(' and temp[len(temp)-1]==')') and (topStack(stackArr)[0]=='(' and topStack(stackArr)[len(topStack(stackArr))-1]==')')):
                    pushVal ="("+topStack(stackArr)[1:len(topStack(stackArr))-1] + x + temp[1:len(temp)-1]+")"
                    flag=1
                elif(temp[0]=='(' and temp[len(temp)-1]==')'):
                    flag=1
                    pushVal ="("+topStack(stackArr) + x + temp[1:len(temp)-1]+")"
                elif(topStack(stackArr)[0]=='(' and topStack(stackArr)[len(topStack(stackArr))-1]==')'):
                    flag=1
                    pushVal="("+topStack(stackArr)[1:len(topStack(stackArr))-1] + x + temp+")"
            if(x=='-'):
                 if((temp[0]=='(' and temp[len(temp)-1]==')') and (topStack(stackArr)[0]=='(' and topStack(stackArr)[len(topStack(stackArr))-1]==')')):
                     pushVal ="("+topStack(stackArr)[1:len(topStack(stackArr))-1] + x + temp+")"
                     flag=1
                 elif(topStack(stackArr)[0]=='(' and topStack(stackArr)[len(topStack(stackArr))-1]==')'):
                     flag=1
                     pushVal="("+topStack(stackArr)[1:len(topStack(stackArr))-1] + x + temp+")"
                 
            if((temp=='0' or temp=='1') and x=='^'):
                if(temp=='0'):
                    pushVal='1'
                else:
                    pushVal=topStack(stackArr)
            elif((temp=='0' or topStack(stackArr)=='0') and (x=='*' or x=='/')):
                pushVal='0'
            else:
                if(flag==0):
                    pushVal ="("+topStack(stackArr) + x + temp+")"
                if(pushVal[1:3]=='0+' or pushVal[1:3]=='1*'):
                    pushVal=pushVal[3:]
                    pushVal=pushVal[:len(pushVal)-1]
                elif(pushVal[len(pushVal)-3:len(pushVal)-1]=='+0' or pushVal[len(pushVal)-3:len(pushVal)-1]=='*1'):
                    pushVal=pushVal[1:]
                    pushVal=pushVal[:len(pushVal)-3]
            pop_stack(stackArr)
            push_stack(stackArr,pushVal)
        else:
            temp=topStack(stackArr)
            pop_stack(stackArr)
            if(temp[0]=='(' and temp[len(temp)-1]==')'):
                pushVal=x+temp
            else:
                pushVal=x+"("+temp+")"
            push_stack(stackArr,pushVal)
    if('+-' in topStack(stackArr)):
        topStack(stackArr).replace('+-','-')
    return(topStack(stackArr))

