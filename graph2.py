import math
from numpy import *
import matplotlib.pyplot as plt
import extract

plt.figure()

def test(text1,text2,t1,t2,text3,text4,item):
    n=50*(t2-t1)/2
    x2=linspace(t1,t2,n)
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
        plt.figure()
        plt.plot(y1,y2)
        plt.savefig("example.png")
    if item==1:
        plt.xlabel(text3)
        plt.ylabel(text4)
        for i in range(len(x2)):
            z=[x2[i]]
            y2[i]=extract.main(text1,z)
            #y1[i]=extract.main(text2,z)
        plt.figure()
        plt.plot(x2,y2)
        plt.savefig("example.png")
    if item==3:
        plt.xlabel(text3)
        plt.ylabel(text4)
        for i in range(len(x2)):
            z=[x2[i]]
            y2[i]=extract.main(text1,z)
            #y1[i]=extract.main(text2,z)
        plt.figure()
        plt.plot(x2,y2)
        plt.savefig("example.png")
    if item==2:
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        for i in range(len(x2)):
            z=[x2[i]]
            y2[i]=extract.main(text1,z)
            y1[i]=extract.main(text2,z)
        plt.figure()
        plt.plot(x2,y2,label=text3)
        plt.plot(x2,y1,label=text4)
        plt.savefig("example.png")
        

