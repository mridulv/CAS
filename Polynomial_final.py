from symbolic import *
import math
class Polynomial:
    def definePoly(self,poly):
        temp=poly
        poly=[]
        poly=temp
        if(poly[0]!='-'):
            poly='+'+poly
        poly=poly+'+'
        length=len(poly)
        a_ind=[]
        a_ind.append(0)
        for i in range(1,length):
            if((poly[i]=='+' or poly[i]=='-')and poly[i-1]!='e'):
                a_ind.append(i)
        a_coeff=[]
        for j in range(0,100):
            a_coeff.append(0)
        counter=0
        for item in a_ind:
            if(a_ind[counter]<length-1):
               sub=poly[a_ind[counter]+1:a_ind[counter+1]]
               if(sub[0]=='x'):
                   sub='1'+sub
               len_sub=len(sub)
               pos=-110
               for k in range(0,len_sub):
                  if(sub[k]=='x'):
                    pos=k
               if(poly[a_ind[counter]]=='+'):
                    b=1
               else:
                    b=-1
               if(pos==-110):
                      a_coeff[0]=b*float(sub)
               elif(pos==(len_sub-1)):
                  sub=sub[0:pos]
                  a_coeff[1]=b*float(sub)
               else:
                   a_coeff[int(sub[pos+2:len_sub])]=b*float(sub[0:pos])
            counter=counter+1
        for i in range(len(a_coeff)):
            if(math.fabs(a_coeff[i])<0.0001):
                a_coeff[i]=0
        return a_coeff

    def formattedPoly(self,poly):
        if(not('x' in poly)):
            return poly
        coeff=[]
        coeff=self.definePoly(poly)
        degree=self.degreeOfPolynomial(coeff)
        output_poly=''
        for i in range (0,degree+1):
            if(coeff[i]!=0):
                if(coeff[i]>0):
                    if(coeff[i]==1):
                        output_poly+="+x^"+str(i)
                    else:
                        output_poly+="+"+str(coeff[i])+"x^"+str(i)
                else:
                    if(coeff[i]==-1):
                        output_poly+="-x^"+str(i)
                    else:
                        output_poly+=str(coeff[i])+"x^"+str(i)
        if('x^0' in output_poly):
            if(output_poly[output_poly.find("x^0")-1]!='+' or output_poly[output_poly.find("x^0")-1]!='-'):
                output_poly=output_poly.replace("x^0","")
            else:
                output_poly=output_poly.replace("x^0","1.0")
        if('x^1+' in output_poly):
            output_poly=output_poly.replace("x^1+","x+")
        if('x^1-' in output_poly):
            output_poly=output_poly.replace("x^1-","x-")
        if(output_poly[0]=="+"):
            output_poly=output_poly[1:]
        return output_poly

    def PolynomialFromCoeff(self,coeff):
        degree=len(coeff)-1
        output_poly=''
        flag=0
        if(degree==0):
            return str(coeff[0])
        for i in range(0,degree+1):
            if(coeff[i]!=0):
                flag=1
                if(coeff[i]>0):
                    if(coeff[i]==1):
                        output_poly+="+x^"+str(i)
                    else:
                        output_poly+="+"+str(coeff[i])+"x^"+str(i)
                else:
                    if(coeff[i]==-1):
                        output_poly+="-x^"+str(i)
                    else:
                        output_poly+=str(coeff[i])+"x^"+str(i)
        if(flag==0):
            output_poly="0"
        if(output_poly[0]=="+"):
            output_poly=output_poly[1:]
        return output_poly

    def degreeOfPolynomial(self,a_coeff):
        degree=0
        for i in range(0,100):
            if(a_coeff[i]!=0):
                degree=i
        return degree

    def MultiplyPolynomial(self,poly1,poly2):
        coeff1=[]
        coeff2=[]
        coeff1=self.definePoly(poly1)
        coeff2=self.definePoly(poly2)
        d1=self.degreeOfPolynomial(coeff1)
        d2=self.degreeOfPolynomial(coeff2)
        final_coeff=[]
        for i in range(0,d1+d2+1):
            final_coeff.append(0)
        i=0
        while(i<=d1):
            j=0
            while(j<=d2):
                final_coeff[i+j]+=(coeff1[i]*coeff2[j])
                j=j+1
            i=i+1
        output_poly=''
        flag=1
        for i in range(0,d1+d2+1):
            if(final_coeff[i]!=0):
                flag=0
                if(final_coeff[i]>0):
                    if(final_coeff[i]==1):
                        output_poly+="+x^"+str(i)
                    else:
                        output_poly+="+"+str(final_coeff[i])+"x^"+str(i)
                else:
                    if(final_coeff[i]==-1):
                        output_poly+="-x^"+str(i)
                    else:
                        output_poly+=str(final_coeff[i])+"x^"+str(i)
        if(flag==1):
            output_poly="0"
            return output_poly
        if(output_poly[0]=="+"):
            output_poly=output_poly[1:]
        prod=(output_poly)
        return prod

    def addPolynomial(self,poly1,poly2):
        newpoly1=[]
        newpoly2=[]
        newpoly1=self.definePoly(poly1)
        newpoly2=self.definePoly(poly2)
        coeff=[]
        d1=self.degreeOfPolynomial(newpoly1)
        d2=self.degreeOfPolynomial(newpoly2)
        i=0
        while(i<=d1 or i<=d2):
            if(i<=d1 and i<=d2):
                coeff.append((newpoly1[i]+newpoly2[i]))
            elif(i>d1 and i<=d2):
                coeff.append(newpoly2[i])
            elif(i>d2 and i<=d1):
                coeff.append(newpoly1[i])
            i=i+1
        output=''
        if (len(coeff)==1):
            output+=str(coeff[0])
            return output
        output=self.PolynomialFromCoeff(coeff)
        add=(output)
        return add

    def subtractPolynomial(self,poly1,poly2):
        newpoly2=self.definePoly(poly2)
        for i in range(0,len(newpoly2)-1):
               newpoly2[i]=0-newpoly2[i]
        poly2=self.PolynomialFromCoeff(newpoly2)
        output=''
        output=self.addPolynomial(poly1,poly2)
        if(output==''):
            return '0'
        return(output)

    def dividePolynomial(self,poly1,poly2,quot=''):
        newpoly1=[]     
        newpoly2=[]
        newpoly1=self.definePoly(poly1)
        newpoly2=self.definePoly(poly2)
        d1=self.degreeOfPolynomial(newpoly1)
        d2=self.degreeOfPolynomial(newpoly2)
        try:
            if(d1<d2):
                return("0",poly1)
            else:
                quot+=str(newpoly1[d1]/newpoly2[d2])+"x^"+str(d1-d2)
                poly1=self.subtractPolynomial(poly1,self.MultiplyPolynomial(quot,poly2))
                newpoly1=self.definePoly(poly1)
                d1=self.degreeOfPolynomial(newpoly1)
                while(d1>=d2):
                    x=(newpoly1[d1]/newpoly2[d2])
                    temp=str(newpoly1[d1]/newpoly2[d2])+"x^"+str(d1-d2)
                    if(x>0):
                       quot+="+"+temp
                       if(poly1==self.MultiplyPolynomial(temp,poly2)):
                          poly1="0" 
                          break
                       poly1=self.subtractPolynomial(poly1,self.MultiplyPolynomial(temp,poly2))
                       newpoly1=self.definePoly(poly1)
                       d1=self.degreeOfPolynomial(newpoly1)
                    else:
                       quot+=temp
                       if(poly1==self.MultiplyPolynomial(temp,poly2)):
                          poly1="0"
                          break
                       poly1=self.subtractPolynomial(poly1,self.MultiplyPolynomial(temp,poly2))
                       newpoly1=self.definePoly(poly1)
                       d1=self.degreeOfPolynomial(newpoly1)  
            quot1=(quot)
            if(poly1!="0"):
               polyn=(poly1)
            else:
               polyn="0"
            return(quot1,polyn)
        except:
            return("unexpected divisor encountered","unexpected divisor encountered")

obj=Polynomial()
def OrthoNormalPolynomial(n):
    n=n+1
    polyn=[]
    polyn.append("1")
    for i in range(1,n):
        polyn.append("x^"+str(i))
        for j in range(i-1):
            val=integrate((obj.MultiplyPolynomial("x^"+str(i),polyn[j])),-1,1)/integrate((obj.MultiplyPolynomial(polyn[j],polyn[j])),-1,1)
            if(val>0.01):
                polyn[i]=obj.subtractPolynomial(polyn[i],obj.MultiplyPolynomial(str(val),polyn[j]))
        polyn[i]=obj.MultiplyPolynomial(polyn[i],str(1/sum(obj.definePoly(polyn[i]))))
        polyn[i]=(polyn[i])
    return polyn

#print(OrthoNormalPolynomial(4))
#print(obj.dividePolynomial("-1","x"))



    

            

    
        
     

        
