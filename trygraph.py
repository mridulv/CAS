import math
from numpy import *
from pylab import *
import extract

def test(text1,text2,t1,t2,text3,text4,item):
    x2=arange(t1,t2,0.01)
    y1=zeros(len(x2))
    y2=zeros(len(x2))
    z=[None]
    if item==0:
        plt.xlabel(text3)
        plt.ylabel(text4)
        for i in range(len(x2)):
            z=[x2[i]]
            y2[i]=extract.main(text1,z)
            y1[i]=extract.main(text2,z)
        plot(y2,y1)
        xlabel(text3)
        ylabel(text4)
        title('f(x) vs g(x)')
        show()
    if item==1:
        xlabel(text3)
        ylabel(text4)
        for i in range(len(x2)):
            z=[x2[i]]
            y2[i]=extract.main(text1,z)
            #y1[i]=extract.main(text2,z)
        plot(x2,y2)
        title('f(x) vs x')
        show()
    if item==3:
        xlabel(text3)
        ylabel(text4)
        for i in range(len(x2)):
            z=[x2[i]]
            y2[i]=extract.main(text1,z)
            #y1[i]=extract.main(text2,z)
        plot(x2,y2)
        title('g(x) vs x')
        show()
    if item==2:
        xlabel(text3)
        ylabel(text4)
        for i in range(len(x2)):
            z=[x2[i]]
            y2[i]=extract.main(text1,z)
            y1[i]=extract.main(text2,z)
        plot(x2,y2)
        plot(x2,y1)
        title('g(x) vs x')
        show()
        

test('x^8','x',2,5,'mri','dul',1)
