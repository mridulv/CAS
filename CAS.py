import wx
import wx.html as html
from Polynomial_final import Polynomial
import regression
import symbolic 
import extract
import diffeqn
import optimize
import math
from numpy import *
import qr_decomposition2
import qr_decomposition
import eigen
import hcf
import graph
import scipy as Sci
import ludecomposition
import gauss
from picture import *
from Fourier import *
import determinant

ID_TRE=-1
ID_TRE2=-2
ID_TRE3=-3
        
class CAS(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(1000,700))

        menubar = wx.MenuBar()
        About = wx.Menu()
        Options = wx.Menu()
        graphplotting=wx.Menu() 
        
        self.SetMenuBar(menubar)

        close= wx.MenuItem(Options, 1, '&close\tCtrl+L')
        Options.AppendItem(close)
        self.Bind(wx.EVT_MENU, self.onclose, id=1)

        refresh= wx.MenuItem(Options, 2, '&refresh\tCtrl+U')
        Options.AppendItem(refresh)
        self.Bind(wx.EVT_MENU, self.onrefresh, id=2)

        clear= wx.MenuItem(Options, 3, '&clear\tCtrl+E')
        Options.AppendItem(clear)
        self.Bind(wx.EVT_MENU, self.onclear, id=3)

        about= wx.MenuItem(About, 4, '&about\tCtrl+H')
        About.AppendItem(about)
        self.Bind(wx.EVT_MENU, self.onabout, id=4)

        Plotyvsx= wx.MenuItem(graphplotting, 5, '&Plotting Graph\tCtrl+O')
        graphplotting.AppendItem(Plotyvsx)
        self.Bind(wx.EVT_MENU, self.plotting, id=5)
    
        menubar.Append(Options, '&Options')
        menubar.Append(About, '&About')
        menubar.Append(graphplotting,'&Graph Plotting')
        sizer2 = wx.GridBagSizer(9, 100)
        
        panel2=wx.Panel(self, -1)
        vbox=wx.BoxSizer(wx.VERTICAL)
        
        self.k=0;
        
        matrices=['A+B','A-B','A.B','Ax=B','A^-1','Determinant','Rank of Matrix','Gauss eliminated matrix','LUD Decomposition','A Tran.','QR decomposition','Eigenvalues','eigenvector','']
        polynomials=['f(x)+g(x)','f(x)-g(x)','f(x).g(x)','g(x) divides f(x)','']
        plotting=['Plot y vs x','plot x vs y','']
        diff=['Deri.At a point','Symbolic differen.','direc. derivative','laplacian','']
        inte=['single D integration','multi D integration','ordinary differential eq.','partial differential equa.','']
        numb=['Sin coefficient','Cos Coefficient','Complex Coefficient','Discrete fourier','Inverse fourier','']
        stats=['least square method','plane fit','exponential curve fitting','logarithmic curve fitting','spline interfolation','spearsman','pearson','kindlestau','']
        exp=['roots in a interval','roots(guess values)','value of exp at a point','']
        opt=['maxima','minima','']
    

        

        sizer = wx.GridBagSizer(4,4)
        
        t1=wx.StaticText(panel2,-1,'History')
        t1.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.BOLD))
        t1.SetForegroundColour('#000000')
        sizer.Add(t1, (0, 25), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)
        #vbox.Add(t1,1,wx.EXPAND | wx.LEFT | wx.TOP | wx.BOTTOM ,wx.ALIGN_CENTER,20)

        self.cont = []
        self.imp= wx.ListBox(panel2, 26,(840,50),(140,500),self.cont, wx.LB_SINGLE)
        #sizer.Add(self.imp, (1,25), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)
        #vbox.Add(self.imp,1,wx.EXPAND)
        
        b1=wx.Button(panel2,-1,'Add this to text box1',pos=(840,550),size=(150,25))
        self.Bind(wx.EVT_BUTTON,self.win1,id=b1.GetId())
        vbox.Add(b1,1,wx.EXPAND)
        #sizer.Add(b1, (19, 25), flag=wx.LEFT, border=5)
        b1.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))

        b2=wx.Button(panel2,-1,'Add this to text box2',pos=(840,580),size=(150,25))
        self.Bind(wx.EVT_BUTTON,self.win2,id=b2.GetId())
        #vbox.Add(b2,1,wx.EXPAND)
        #sizer.Add(b2, (20, 25), flag= wx.LEFT , border=5)
        b2.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))
        

        b3=wx.Button(panel2,-1,'Delete this entry',pos=(840,610),size=(150,25))
        self.Bind(wx.EVT_BUTTON,self.win3,id=b3.GetId())
        #vbox.Add(b3,1,wx.EXPAND)
        #sizer.Add(b3, (21, 25), flag=wx.LEFT, border=5)
        b3.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))



        
        self.text1 = wx.StaticText(panel2, -1, 'Text box1=')
        self.text1.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))
        panel2.SetBackgroundColour('#aaaaaa')
        sizer.Add(self.text1, (0, 0), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)
        
        self.tc = wx.TextCtrl(panel2, -1,pos=(10,30),size=(750,30))
        #sizer.Add(self.tc, (1, 0), (1, 18), wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        self.tc.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL,wx.BOLD))
        
        
        k=wx.StaticBox(panel2, -1, 'MatheMatical Operations', (10,140), size=(750,386))
        k.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))

        self.text2 = wx.StaticText(panel2, -1, 'Text box2=')
        self.text2.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))
        sizer.Add(self.text2, (2, 0), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)
        
        self.tc2 = wx.TextCtrl(panel2, -1,pos=(10,100),size=(750,30))
        #sizer.Add(self.tc2, (3, 0), (1, 18), wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        self.tc2.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL,wx.BOLD))

        text3 = wx.StaticText(panel2, -1, 'Matrices  ')
        text3.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))
        sizer.Add(text3, (7,1), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)

        self.combo = wx.ComboBox(panel2, -1,choices=matrices,style=wx.CB_READONLY )
        sizer.Add(self.combo, (7,3), (1, 3), wx.TOP | wx.EXPAND, 5)
        self.Bind(wx.EVT_COMBOBOX, self.OnSelect,id=self.combo.GetId())


        text4 = wx.StaticText(panel2, -1, 'Diff. Calculus')
        text4.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))
        sizer.Add(text4, (7,10), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)

        self.combo2 = wx.ComboBox(panel2, -1,choices=diff,style=wx.CB_READONLY)
        sizer.Add(self.combo2, (7,13), (1, 3), wx.TOP | wx.EXPAND, 5)
        self.Bind(wx.EVT_COMBOBOX, self.OnSelect2,id=self.combo2.GetId())


        text5 = wx.StaticText(panel2, -1, 'Polynomials  ')
        text5.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))
        sizer.Add(text5, (10,1), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)

        self.combo3 = wx.ComboBox(panel2, -1,choices=polynomials,style=wx.CB_READONLY)
        sizer.Add(self.combo3, (10,3), (1,3), wx.TOP | wx.EXPAND, 5)
        self.Bind(wx.EVT_COMBOBOX, self.OnSelect3,id=self.combo3.GetId())



        text6 = wx.StaticText(panel2, -1, 'Int. Calculus')
        text6.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))
        sizer.Add(text6, (10,10), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)

        self.combo4 = wx.ComboBox(panel2, -1,style=wx.CB_READONLY ,choices=inte)
        sizer.Add(self.combo4, (10,13), (1, 3), wx.TOP | wx.EXPAND, 5)
        self.Bind(wx.EVT_COMBOBOX, self.OnSelect4,id=self.combo4.GetId())


        
        text7 = wx.StaticText(panel2, -1, 'Fourier Analysis')
        text7.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))
        sizer.Add(text7, (13,1), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)

        self.combo5 = wx.ComboBox(panel2, -1,style=wx.CB_READONLY ,choices=numb)
        sizer.Add(self.combo5, (13,3), (1, 3), wx.TOP | wx.EXPAND, 5)
        self.Bind(wx.EVT_COMBOBOX, self.OnSelect5,id=self.combo5.GetId())


        text8 = wx.StaticText(panel2, -1, 'Statistics')
        text8.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))
        sizer.Add(text8, (13,10), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)

        self.combo6 = wx.ComboBox(panel2, -1,style=wx.CB_READONLY,choices=stats)
        sizer.Add(self.combo6, (13,13), (1, 3), wx.TOP | wx.EXPAND, 5)
        self.Bind(wx.EVT_COMBOBOX, self.OnSelect6,id=self.combo6.GetId())


        
        text9 = wx.StaticText(panel2, -1, 'Optimization')
        text9.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))
        sizer.Add(text9, (16,1), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)

        self.combo7 = wx.ComboBox(panel2, -1,style=wx.CB_READONLY,choices=opt )
        sizer.Add(self.combo7, (16,3), (1, 3), wx.TOP | wx.EXPAND, 5)
        self.Bind(wx.EVT_COMBOBOX, self.OnSelect7,id=self.combo7.GetId())


        text10 = wx.StaticText(panel2, -1, 'Solving Exp. ')
        text10.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))
        sizer.Add(text10, (16,10), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)

        self.combo8 = wx.ComboBox(panel2, -1, style=wx.CB_READONLY,choices=exp)
        sizer.Add(self.combo8, (16,13), (1, 3), wx.TOP | wx.EXPAND, 5)
        self.Bind(wx.EVT_COMBOBOX, self.OnSelect8,id=self.combo8.GetId())



        text11 = wx.StaticText(panel2, -1, 'Answer-:')
        sizer.Add(text11, (19, 0), flag=wx.LEFT, border=10)
        text11.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))

        self.text12 = wx.TextCtrl(panel2, -1, size=(-1, 30))
        sizer.Add(self.text12, (20,0), (1,18), wx.TOP | wx.EXPAND | wx.BOTTOM | wx.LEFT, 5)
        self.text12.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD))
        
        b12=wx.Button(panel2, -1, 'Compute:-')
        sizer.Add(b12, (22,0), flag=wx.LEFT | wx.BOTTOM, border=10)
        self.Bind(wx.EVT_BUTTON,self.answer,id=b12.GetId())
        b12.SetFont(wx.Font(13, wx.SWISS, wx.NORMAL, wx.BOLD))
        b12.SetForegroundColour('#000000')


        #sizer2.Add(sizer,(0,0),flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)
        #panel2.SetSizer(sizer2)
        
        
        panel2.SetSizer(sizer)
        self.Centre()
        self.Show(True)

    def OnSelect(self,event):
        self.tc.SetValue('')
        self.text1.SetLabel('Text Box1')
        self.text2.SetLabel('Text box2')
        self.tc2.SetValue('')
        self.text12.SetValue('')
        item=event.GetSelection()
        print item
        if item<=3:
            self.text1.SetLabel('A=')
            self.text2.SetLabel('B=')
        else:
            self.text1.SetLabel('A=')
            self.text2.SetLabel(''
                            )
        self.k=item
        print self.k
        
        self.combo3.SetValue('')
        self.combo2.SetValue('')
        self.combo4.SetValue('')
        self.combo5.SetValue('')
        self.combo6.SetValue('')
        self.combo7.SetValue('')
        self.combo8.SetValue('')
        
    def OnSelect2(self,event):
        self.tc.SetValue('')
        self.text1.SetLabel('Text Box1')
        self.text2.SetLabel('Text box2')
        self.tc2.SetValue('')
        self.text12.SetValue('')
        item=event.GetSelection()
        print item
        self.text1.SetLabel('f(x)')
        if item==0:
            self.text2.SetLabel('Enter the point where the deri.is to be found')
            self.tc2.SetValue('[enter the x, which derivative]')
        if item==1: 
            self.text2.SetLabel('Enter the variable wrt the derivative is to be found')
            self.tc2.SetValue('enter the variable')
        if item==2:
            self.text2.SetLabel('enter the point and the direction')
            self.tc2.SetValue('[[enter the point],[enter the direction]]')
        if item==3:
            self.text2.SetLabel('')
        self.k=item+16
        print self.k
        self.combo.SetValue('')
        self.combo3.SetValue('')
        self.combo4.SetValue('')
        self.combo5.SetValue('')
        self.combo6.SetValue('')
        self.combo7.SetValue('')
        self.combo8.SetValue('')

    def OnSelect3(self,event):
        self.tc.SetValue('')
        self.text1.SetLabel('Text Box1')
        self.text2.SetLabel('Text box2')
        self.tc2.SetValue('')
        self.text12.SetValue('')
        item=event.GetSelection()
        print item
        self.text1.SetLabel('f(x)=')
        self.text2.SetLabel('g(x)=')
        if item==25:
            self.text2.SetLabel('')
        self.k=item+21
        print self.k
        self.combo.SetValue('')
        self.combo2.SetValue('')
        self.combo4.SetValue('')
        self.combo5.SetValue('')
        self.combo6.SetValue('')
        self.combo7.SetValue('')
        self.combo8.SetValue('')
        
    def OnSelect4(self,event):
        self.tc.SetValue('')
        self.text1.SetLabel('Text Box1')
        self.text2.SetLabel('Text box2')
        self.tc2.SetValue('')
        self.text12.SetValue('')
        item=event.GetSelection()
        print item
        self.text1.SetLabel('f(x)=')
        self.text2.SetLabel('Limits')
        if item==0:
            self.tc2.SetValue('[enter the lower limit,enter the upper limit]')
        if item==1:
            self.tc2.SetValue('[[lower limit of first,upperof first],[lower of second,upper of second] and so on...]')
        if item==2:
            self.tc2.SetValue('[initial conditions,x initial,x final')
        if item==3:
            self.tc2.SetValue('[[conditions at the origin],[boundary point],[bounary conditions at this point],[point at which fn. to be calculated]')
        self.k=item+27
        print self.k
        self.combo.SetValue('')
        self.combo3.SetValue('')
        self.combo2.SetValue('')
        self.combo5.SetValue('')
        self.combo6.SetValue('')
        self.combo7.SetValue('')
        self.combo8.SetValue('')

    def OnSelect5(self,event):
        self.tc.SetValue('')
        self.text1.SetLabel('Text Box1')
        self.text2.SetLabel('Text box2')
        self.tc2.SetValue('')
        self.text12.SetValue('')
        item=event.GetSelection()
        print item
        if item<=2:
            self.text1.SetLabel('Enter The Function')
            self.text2.SetLabel('Enter The Nth coefficient and the interval in which the function is periodic')
            self.tc2.SetValue('[Enter the cooefficient,lower limit of the interval of periodicity,upper limit of the interval]')
        else:
            self.text1.SetLabel('Enter The Group of points')
            self.text2.SetLabel('')
        self.k=item+32
        print self.k
        self.combo.SetValue('')
        self.combo3.SetValue('')
        self.combo2.SetValue('')
        self.combo4.SetValue('')
        self.combo6.SetValue('')
        self.combo7.SetValue('')
        self.combo8.SetValue('')

    def OnSelect6(self,event):
        self.tc.SetValue('')
        self.text1.SetLabel('Text Box1')
        self.text2.SetLabel('Text box2')
        self.tc2.SetValue('')
        self.text12.SetValue('')
        item=event.GetSelection()
        print item
        self.text1.SetLabel('Enter the group of points')
        self.text2.SetLabel('')
        if item==0:
             self.text1.SetLabel('Enter the group of points')
             self.text2.SetLabel('Enter the degree of polynomial you want')
        self.k=item+37
        print self.k
        self.combo.SetValue('')
        self.combo3.SetValue('')
        self.combo2.SetValue('')
        self.combo4.SetValue('')
        self.combo5.SetValue('')
        self.combo7.SetValue('')
        self.combo8.SetValue('')

    def OnSelect7(self,event):
        self.tc.SetValue('')
        self.text1.SetLabel('Text Box1')
        self.text2.SetLabel('Text box2')
        self.tc2.SetValue('')
        self.text12.SetValue('')
        item=event.GetSelection()
        print item
        self.text1.SetLabel('optimization')
        self.text2.SetLabel('Enter the ranges for which you want to find min. or max.')
        self.tc2.SetValue('[[enter the lower of first,enter the upper of first],[enter the lower of second ,enter the upper of second] and so on..] ')
        self.k=item+46 
        print self.k
        self.combo.SetValue('')
        self.combo3.SetValue('')
        self.combo2.SetValue('')
        self.combo4.SetValue('')
        self.combo5.SetValue('')
        self.combo6.SetValue('')
        self.combo8.SetValue('')

    def OnSelect8(self,event):
        self.tc.SetValue('')
        self.text1.SetLabel('Text Box1')
        self.text2.SetLabel('Text box2')
        self.tc2.SetValue('')
        self.text12.SetValue('')
        item=event.GetSelection()
        print item
        if item==2:
           self.text1.SetLabel('Enter the expression')
           self.text2.SetLabel('Enter the point of which you want the value in the form of array')
        else:
            self.text1.SetLabel('Enter the expression')
            self.text2.SetLabel('Enter the interval')
        self.k=item+49
        print self.k
        self.combo.SetValue('')
        self.combo3.SetValue('')
        self.combo2.SetValue('')
        self.combo4.SetValue('')
        self.combo5.SetValue('')
        self.combo6.SetValue('')
        self.combo7.SetValue('')
    

    def win1(self,event):
        sel=self.imp.GetSelection()
        text=self.imp.GetString(sel)
        print text
        self.tc.SetLabel(text)
    
    def win2(self,event):
        sel= self.imp.GetSelection()
        text= self.imp.GetString(sel)
        print text
        self.tc2.SetLabel(text)

    def win3(self,event):
        sel= self.imp.GetSelection()
        text= self.imp.GetString(sel)
        print text
        self.imp.Delete(sel)
        
            

    def onclose(self,event):
        self.Close()
    def onclear(self,event):
        text= self.imp.GetString()
        k=len(self.cont)
        while k:
            self.imp.Delete(0)
            text= self.imp.GetString(0)
            k=k-1

    def plotting(self,event):
        page2(None,-1,'Graph Plotter')
        #text=self.tc.GetValue()
        #text2=self.tc2.GetValue()
        #text3= wx.GetTextFromUser('Enter the interval in which you want the graph to be format:[a,b]', 'Interval of the graph')
        #c=self.conv(text3)
        #print c[0],c[1]
        #self.text1.SetLabel('f(x)')
        #self.text2.SetLabel('g(x)')
        #self.imp.Append(text)
        #self.imp.Append(text2)
        #graph.test(text,text2,c[0],c[1])
        
    def onrefresh(self,event):
        self.tc.SetValue('')
        self.text1.SetLabel('Text Box1')
        self.text2.SetLabel('Text box2')
        self.tc2.SetValue('')
        self.text12.SetValue('')
        self.combo.SetValue('')
        self.combo3.SetValue('')
        self.combo2.SetValue('')
        self.combo4.SetValue('')
        self.combo5.SetValue('')
        self.combo6.SetValue('')
        self.combo7.SetValue('')
        self.combo8.SetValue('')
        
    def onabout(self,event):
        page(self,-1,'info regarding how to give input')


    def answer(self,event):
        f=open("data.txt",'w')
        t1=self.tc.GetValue()
        t2=self.tc2.GetValue()
        self.imp.Append(t1)
        f.write(t1+'\n')
        self.imp.Append(t2)
        f.write(t2+'\n')
        print self.k
        if self.k<=5 and self.k>=0:                                                          # matrices (part 1)
            text=self.tc.GetValue()
            print(text)
            a=self.conv(text)
            text2=self.tc2.GetValue()
            print(text2)
            b=self.conv(text2)
            if self.k==0:
              try:
                    ans=matrix(a)+matrix(b)
                    ans=str(ans)
                    self.text12.SetValue(ans)
              except:
                ans='Either of the matrix is not given in the correct format' 
                self.text12.SetValue(ans)
            if self.k==1:
              try:
                ans=matrix(a)-matrix(b)
                ans=str(ans)
                self.text12.SetValue(ans)
              except:
                ans='Either of the matrix is not given in the correct format' 
                self.text12.SetValue(ans)
            if self.k==2:
              try:
                ans=dot(matrix(a),matrix(b))
                ans=str(ans)                                         
                self.text12.SetValue(ans)
              except:
                ans='Either of the matrix is not given in the correct format' 
                self.text12.SetValue(ans)
            if self.k==3:
              try:
               if determinant.determinant(a)!=0:   
                v=matrix(a).I
                ans=dot(v,matrix(b))
                ans=str(ans)
                self.text12.SetValue(ans)
               elif determinant.determinant(a)==0:
                ans='Given an invertible matrix'
                self.text12.SetValue(ans)  
              except:
                ans='Either of the matrix is not given in the correct format' 
                self.text12.SetValue(ans)  
            if self.k==4:
              try:  
               if determinant.determinant(a)!=0:
                ans=matrix(a).I
                ans=str(ans)
                self.text12.SetValue(ans)
               elif determinant.determinant(a)==0:
                ans='The matrix is not invertible'
                self.text12.SetValue(ans)
              except:
                ans='The matrix is not given inthe correct format'
                self.text12.SetValue(ans)  
            if self.k==5:
               try: 
                c=determinant.determinant(a)
                ans=str(c)
                self.text12.SetValue(ans)
               except:
                ans='The matrix given is not in the correct format'
                self.text12.SetValue(ans)
                
        if self.k>5 and self.k<=14 :
            self.text2.SetLabel('')
            text=self.tc.GetValue()                                                # matrices (part 2)
            print(text)
            a=self.conv(text)
            if self.k==6:
              try:
                a=matrix(a)
                m=rank(a)
                m=str(m)
                self.text12.SetValue(m)
              except:
                m='The given input is not in the correct format'
                self.text12.SetValue(m)
            if self.k==7:
              try:
                c=matrix(a)
                ans=gauss.test(c,len(a))
                ans=str(ans)
                self.text12.SetValue(ans)
              except:
                ans='The given input is not in the correct format'
                self.text12.SetValue(ans)
            if self.k==8:
              try:
                l,u,d=ludecomposition.test(a)
                ans='l is ',l,'u is',u,'and d is',d
                ans=str(ans)
                self.text12.SetValue(ans)
              except:
                ans='The given input is not in the correct format'
                self.text12.SetValue(ans)
            if self.k==9:
              try:
                ans=matrix(a).T
                ans=str(ans)
                self.text12.SetValue(ans)
              except:
                ans='The given input is not in the correct format'
                self.text12.SetValue(ans)  
            if self.k==10:
              try:
                a=matrix(a)
                ans1,ans2=qr_decomposition.test(text)
                ans='Q is ',ans1,'R is ',ans2,'in QR decomposition'
                ans=str(ans)
                self.text12.SetValue(ans)
              except:
                ans='The given input is not correct'
                self.text12.SetValue(ans)
            if self.k==11:
              try:
                ans=qr_decomposition2.test(text)
                ans=str(ans)
                self.text12.SetValue(ans)
              except:
                ans='The given input is not correct'
                self.text12.SetValue(ans)  
            if self.k==12:
              try:
                ans=eigen.test(text)
                ans=str(ans)
                self.text12.SetValue(ans)
              except:
                ans='The given input is incorrect'
                self.text12.SetValue(ans)

        if self.k>=16 and self.k<20:                                            # differential calculus
            text2=self.tc2.GetValue()
            text=self.tc.GetValue()
            if self.k==16:
              try:
                b=self.conv(text2)
                print b[0],b[1]
                ans=symbolic.differentiate(text,float(b[0]),int(b[1]))
                ans=str(ans)
                self.text12.SetValue(ans)
              except:
                ans='please check the input that you have given'
                self.text12.SetValue(ans)
            if self.k==17:
              try:
                ans=symbolic.CallDiff(text,text2)
                ans=str(ans)
                self.text12.SetValue(ans)
              except:
                ans='The given input is not correct'
                self.text12.SetValue(ans)
            if self.k==18:
              try:
                b=self.conv(text2)
                ans=symbolic.dirDeriv(text,b[0],b[1])
                ans=str(ans)
                self.text12.SetValue(ans)
              except:
                ans='The given input is not correct'
                self.text12.SetValue(ans)
            if self.k==19:
              try:
                ans=symbolic.Laplacian(text)
                ans=str(ans)
                self.text12.SetValue(ans)
              except:
                ans='The given input is not correct'
                self.text12.SetValue(ans)
                
        if self.k>=21 and self.k<=25:                                                    # polynomials
            text=self.tc.GetValue()
            text2=self.tc2.GetValue()
            Poly=Polynomial()
            if self.k==21:
              try:
                ans=Poly.addPolynomial(text,text2)
                ans=str(ans)
                self.text12.SetValue(ans)
              except:
                ans='The given input is not correct'
                self.text12.SetValue(ans)
            if self.k==22:
              try:
                ans=Poly.subtractPolynomial(text,text2)
                ans=str(ans)
                self.text12.SetValue(ans)
              except:
                ans='The given input is not correct'
                self.text12.SetValue(ans)
            if self.k==23:
              try:
                ans=Poly.MultiplyPolynomial(text,text2)
                ans=str(ans)
                self.text12.SetValue(ans)
              except:
                ans='The given input is not correct'
                self.text12.SetValue(ans)
            if self.k==24:
              try:
                ans=Poly.dividePolynomial(text,text2)
                ans=str(ans)
                self.text12.SetValue(ans)
              except:
                ans='The given input is not correct'
                self.text12.SetValue(ans)
            if self.k==25:
              try:
                self.tc2.SetValue('')
                ans=rootpoly(text)
                ans=str(ans)                                                           # karna hain
                self.text12.SetValue(ans)
              except:
                ans='he choice not selected'
                self.text12.SetValue(ans)
        if self.k>=27 and self.k<=30:                                                    # integral calculus
            text=self.tc.GetValue()
            text2=self.tc2.GetValue()                                               
            print(text2)

            if self.k==27:
              try:
                b=self.conv(text2)
                lower=[None]*len(b)
                upper=[None]*len(b)
                ans=symbolic.integrate(text,b[0],b[1])
                ans=str(ans)
                self.text12.SetValue(ans)
              except:
                ans='The given input is not correct'
                self.text12.SetValue(ans)
            if self.k==28:
              try:
                b=self.conv3(text2)
                print 'mridul',b
                lower=[None]*len(b)
                upper=[None]*len(b)
                for i in range(len(b)):
                    lower[i]=b[i][0]
                    upper[i]=b[i][1]
                print 'mridul',lower,upper
                ans=symbolic.multiDimensionInteg(text,len(b),lower,upper)
                ans=str(ans)
                self.text12.SetValue(ans)
              except:
                ans='The given input is not correct'
                self.text12.SetValue(ans)
            if self.k==29:
              try:
                b=self.conv(text2)
                lower=[None]*len(b)
                upper=[None]*len(b)
                if len(b)==6:
                    ans=diffeqn.solveDiffEqn4(text,b[:len(b)-2],b[len(b)-2],b[len(b)-1])                        # the first element b[len(b)-1] is the point where the f(x) has to be calculated  and the rest are the initial conditions
                if len(b)==5:
                    ans=diffeqn.solveDiffEqn3(text,b[:len(b)-2],b[len(b)-2],b[len(b)-1])
                if len(b)==4:
                    ans=diffeqn.solveDiffEqn2(text,b[:len(b)-2],b[len(b)-2],b[len(b)-1])                        # the first element b[0] is the point where the f(x) has to be calculated  and the rest are the initial conditions
                if len(b)==3:
                    ans=diffeqn.solveDiffEqn1(text,b[:len(b)-2],b[len(b)-2],b[len(b)-1])
                ans=str(ans)
                self.text12.SetValue(ans)
              except:
                ans='The given input is not in not in the standard format demanded by CAS'
                self.text12.SetValue(ans)
            if self.k==30:
              try:
                b=self.conv3(text2)
                lower=[None]*len(b)
                upper=[None]*len(b)
                print b
                ans=diffeqn.LaplaceEqn(text,b[0],b[2],b[1],b[3])                                        
                ans=str(ans)
                self.text12.SetValue(ans)
              except:
                ans='The given input is not correct'
                self.text12.SetValue(ans)
        if self.k>=37 and self.k<=44:                                             # statistics the data points  
            text=self.tc.GetValue()
            print(text)
            b=self.conv(text)
            lower=[None]*len(b)
            middle=[None]*len(b)
            upper=[None]*len(b)
            if self.k==37:
              try:
                text2=self.tc2.GetValue()
                for i in range(len(b)):
                    lower[i]=b[i][0]
                    upper[i]=b[i][1]
                ans=regression.LeastSquare(int(text2),lower,upper)
                ans=str(ans)
                self.text12.SetValue(ans)
              except:
                ans='The given input is not correct format'
                self.text12.SetValue(ans)
            if self.k==38:
              try:
                for i in range(len(b)):
                    lower[i]=b[i][0]
                    middle[i]=b[i][1]
                    upper[i]=b[i][2]
                ans=regression.PlaneFit(lower,middle,upper)
                ans=str(ans)
                self.text12.SetValue(ans)
              except:
                ans='The given input is not correct'
                self.text12.SetValue(ans)
            if self.k==39:
              try:
                for i in range(len(b)):
                    lower[i]=b[i][0]
                    upper[i]=b[i][1]
                ans=regression.ExponentialCurve(lower,upper)
                ans=str(ans)
                self.text12.SetValue(ans)
              except:
                ans='The given input is not correct'
                self.text12.SetValue(ans)
            if self.k==40:
              try:
                for i in range(len(b)):
                    lower[i]=b[i][0]
                    upper[i]=b[i][1]
                ans=regression.LogarithmicCurve(lower,upper)
                ans=str(ans)
                self.text12.SetValue(ans)
              except:
                ans='The given input is not correct'
                self.text12.SetValue(ans)
            if self.k==41:
              try:
                ans=regression.SplineInterpolation(b)
                ans=str(ans)
                self.text12.SetValue(ans)
              except:
                ans='The given input is not correct'
                self.text12.SetValue(ans)
            if self.k==42:
              try:
                for i in range(len(b)):
                    lower[i]=b[i][0]
                    upper[i]=b[i][1]
                ans=regression.SpearsmanCoff(lower,upper)
                ans=str(ans)
                self.text12.SetValue(ans)
              except:
                ans='The given input is not correct'
                self.text12.SetValue(ans)
            if self.k==43:
              try:
                for i in range(len(b)):
                    lower[i]=b[i][0]
                    upper[i]=b[i][1]
                ans=regression.Pearson(lower,upper)
                ans=str(ans)
                self.text12.SetValue(ans)
              except:
                ans='The given input is not correct'
                self.text12.SetValue(ans)
            if self.k==44:
              try:
                ans=regression.tau(b)
                ans=str(ans)
                self.text12.SetValue(ans)
              except:
                ans='The given input is not correct'
                self.text12.SetValue(ans)  
        if self.k>=32 and self.k<=36:                                        # playing with Fourier
             text=self.tc.GetValue()
             print (text)
             if self.k==32:
              try:
                text2=self.tc2.GetValue()
                b=self.conv(text2)
                ans=SinCoeff(text,b[0],b[1],b[2])
                ans=str(ans)
                self.text12.SetValue(ans)
              except:
                ans='The given input is not correct'
                self.text12.SetValue(ans)
             if self.k==33:
              try:
                text2=self.tc2.GetValue()
                b=self.conv(text2)
                ans=CosCoeff(text,b[0],b[1],b[2])
                ans=str(ans)
                self.text12.SetValue(ans)
              except:
                ans='The given input is not correct'
                self.text12.SetValue(ans)
             if self.k==34:
              try:
                text2=self.tc2.GetValue()
                b=self.conv(text2)
                ans=FourierCoeff(text,b[0],b[1],b[2])
                ans=str(ans)
                self.text12.SetValue(ans)
              except:
                ans='The given input is not correct'
                self.text12.SetValue(ans)
             if self.k==35:
              try:
                b=self.conv2(text)
                ans=discreteFourier(b,len(b))
                ans=str(ans)
                self.text12.SetValue(ans)
              except:
                ans='The given input is not correct'
                self.text12.SetValue(ans)
             if self.k==36:
              try:
                b=self.conv2(text)
                ans=inverseVal(b,len(b))
                ans=str(ans)
                self.text12.SetValue(ans)
              except:
                ans='The given input is not correct'
                self.text12.SetValue(ans)
                
        if self.k>=46 and self.k<=47:                                        # optimization
             text=self.tc.GetValue()
             print (text)
             text2=self.tc2.GetValue()
             b=self.conv(text2)
             lower=[None]*len(b)
             upper=[None]*len(b)
             for i in range(len(b)):
                    lower[i]=b[i][0]
                    upper[i]=b[i][1]
             if self.k==46:
              try:
                m=symbolic.Max(text,len(b),lower,upper)
                ans=str(m)
                self.text12.SetValue(ans)
              except:
                ans='The given input is not correct'
                self.text12.SetValue(ans)
             if self.k==47:
              try:
                m=symbolic.Min(text,len(b),lower,upper)
                ans=str(m)
                self.text12.SetValue(ans)
              except:
                ans='The given input is not correct'
                self.text12.SetValue(ans)
                

        if self.k>=49:                                                      #evaluating expression
            text=self.tc.GetValue()
            print (text)
            text2=self.tc2.GetValue()
            b=self.conv(text2)
            if self.k==49:
              try:
                m=symbolic.roots_interval(text,b[0],b[1])
                ans=str(m)
                self.text12.SetValue(ans)
              except:
                ans='The given input is not correct'
                self.text12.SetValue(ans)
            if self.k==50:
              try:
                m=symbolic.EqnSolver(text,b[0],b[1])
                ans=str(m)
                self.text12.SetValue(ans)
              except:
                ans='The given input is not correct'
                self.text12.SetValue(ans)
            if self.k==51:
              try:
                m=extract.main(text,b)
                ans=str(m)
                self.text12.SetValue(ans)
              except:
                ans='The given input is not correct'
                self.text12.SetValue(ans)
        t3=self.text12.GetValue()
        self.imp.Append(t3)
        f.write(t3+'\n')
        f.close()

    def conv(self,text):
      try:
        k=0
        if text=='':
            return 0
        elif ord(text[0])-ord('0')<=9 and ord(text[0])-ord('0')>=0:
            return int(text)
        else:
            for i in range(len(text)):
                if (text[i]=='['):
                    k=k+1
            l=k
            if(k!=1):
                k=k-1
            lst=list()
            lst=text.split(',')
            print(len(lst))
            for i in range(len(lst)):
                if('[' in lst[i]):
                    lst[i]=lst[i].replace('[','')
                if(']' in lst[i]):
                    lst[i]=lst[i].replace(']','')
            m=k
            print lst
            k=len(lst)/k
            print len(lst)
            print lst
            if l!=1:
                b=[None]*m
                for i in range(m):
                    b[i]=[None]*(len(lst)/m)
                for i in range(len(lst)):
                    n=int(i/k)
                    m=i%k
                    print m,n
                    if lst[i]=='inf' or lst[i]=='+inf':
                        b[n][m]=300.0
                    elif lst[i]=='-inf':
                        b[n][m]=-300.0
                    else:
                        b[n][m]=float(lst[i])
                print b
                return b
                
            
            if l==1:
                b=[None]*len(lst)
                for i in range(len(lst)):
                    if lst[i]=='inf' or lst[i]=='+inf':
                        b[i]=300.0
                    elif lst[i]=='-inf':
                        b[i]=-300.0
                    else:
                        b[i]=float(lst[i])
                return b
      except:
          print 'mrdkms'
          return 'The data given was not in the correct format'

    def conv2(self,text):
     try:   
        k=0
        for i in range(len(text)):
                if (text[i]=='['):
                    k=k+1
        l=k
        if(k!=1):
                k=k-1
        lst=list()
        lst=text.split(',')
        print(len(lst))
        for i in range(len(lst)):
                if('[' in lst[i]):
                    lst[i]=lst[i].replace('[','')
                if(']' in lst[i]):
                    lst[i]=lst[i].replace(']','')
        m=k
        print lst 
        k=len(lst)/k
        print len(lst)
            
        if l==1:
                b=[None]*len(lst)
                for i in range(len(lst)):
                        b[i]=complex(lst[i])

        
                return b
     except:
                return 'The data given was not in the correct format'
            
        
                    
     text2=self.tc2.GetValue()
     self.imp.Append(text)
     self.imp.Append(text2)

    def conv3(self,text):
     try:   
        k=0
        for i in range(len(text)):
                if (text[i]=='['):
                    k=k+1
        l=k
        if(k!=1):
                k=k-1
        lst=list()
        lst=text.split(',')
        print(len(lst))
        for i in range(len(lst)):
                if('[' in lst[i]):
                    lst[i]=lst[i].replace('[','')
                if(']' in lst[i]):
                    lst[i]=lst[i].replace(']','')
        m=k
        print 'mri',lst
        k=len(lst)/k
        print len(lst)

       
        if l!=1:
            b=[None]*m
            for i in range(m):
                b[i]=[None]*(len(lst)/m)
            for i in range(len(lst)):
                n=int(i/k)
                m=i%k
                print m,n
                b[n][m]=lst[i]
            return b
     
            
        if l==1:
                b=[None]*len(lst)
                for i in range(len(lst)):
                        b[i]=lst[i]
                
                return b
     except:
            return 'The data given was not in the correct format'       
            
        
                    
     text2=self.tc2.GetValue()
     self.imp.Append(text)
     self.imp.Append(text2)
        

class page(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(900, 700))


        panel = wx.Panel(self, -1)

        vbox=wx.BoxSizer(wx.VERTICAL)
        panel.SetBackgroundColour(wx.LIGHT_GREY)
        
        htmlwin = html.HtmlWindow(panel, -1, style=wx.NO_BORDER)
        htmlwin.LoadPage('mridul.html')
        

        vbox.Add(htmlwin,1, wx.EXPAND | wx.ALL, 9)
        panel.SetSizer(vbox)
        
       
        self.Center()
        self.Show(True)


class page2(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(850,510))

        panel = wx.Panel(self, -1)
        sizer = wx.GridBagSizer(4,4)

        panel.SetBackgroundColour(wx.LIGHT_GREY)
        
        panel.SetSizer(sizer)

        
        self.k=0
        numb=['Plot graph f(x) vs. g(x)','Plot graph f(x) vs. x','Plot graph f(x) vs. x and plot graph g(x) vs. x','curve Plotting via points']


        f=open("data.txt")
        mri=f.read()
        self.cont=[]
        self.cont=mri.split()
        self.imp= wx.ListBox(panel, 26,(690,30),(135,380),self.cont, wx.LB_SINGLE)
        f.close()
        
        text8 = wx.StaticText(panel, -1, 'Import functions',pos=(690,5))
        text8.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD))
        
        text7 = wx.StaticText(panel, -1, 'Graph Plotting')
        text7.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))
        sizer.Add(text7, (1,1), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)

        self.combo5 = wx.ComboBox(panel, -1,style=wx.CB_READONLY ,choices=numb)
        sizer.Add(self.combo5, (1,4), (1, 3), wx.TOP | wx.EXPAND, 5)
        self.Bind(wx.EVT_COMBOBOX, self.OnSelect3,id=self.combo5.GetId())

        self.text1 = wx.StaticText(panel, -1, 'f(x)=')
        self.text1.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))
        sizer.Add(self.text1, (3, 1), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)
        
        self.tc = wx.TextCtrl(panel, -1)
        sizer.Add(self.tc, (4,1), (1,10), wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        self.tc.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL,wx.BOLD))


        self.text2 = wx.StaticText(panel, -1, 'g(x)=')
        self.text2.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))
        sizer.Add(self.text2, (6,1), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)
        
        self.tc2 = wx.TextCtrl(panel, -1)
        sizer.Add(self.tc2, (7,1), (1,10), wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        self.tc2.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL,wx.BOLD))
        
        self.text3 = wx.StaticText(panel, -1, 'Enter the first number of your interval of x ')
        self.text3.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))
        panel.SetBackgroundColour('#aaaaaa')
        sizer.Add(self.text3, (9,1), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)
        
        self.tc3 = wx.TextCtrl(panel, -1,size=(150,30))
        sizer.Add(self.tc3, (9, 4), (1,7), wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        self.tc3.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL,wx.BOLD))

        self.text4 = wx.StaticText(panel, -1, 'Enter the second number of your interval of x')
        self.text4.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))
        panel.SetBackgroundColour('#aaaaaa')
        sizer.Add(self.text4, (10, 1), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)
        
        self.tc4 = wx.TextCtrl(panel, -1,size=(150,30))
        sizer.Add(self.tc4, (10,4), (1,7), wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        self.tc4.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL,wx.BOLD))

        self.text5 = wx.StaticText(panel, -1, 'Enter the Y label')
        self.text5.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))
        panel.SetBackgroundColour('#aaaaaa')
        sizer.Add(self.text5, (11,1), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)
        
        self.tc5 = wx.TextCtrl(panel, -1,size=(150,30))
        sizer.Add(self.tc5, (11,4), (1,7), wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        self.tc5.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL,wx.BOLD))

        self.text6 = wx.StaticText(panel, -1, 'Enter the X label')
        
        self.text6.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))
        panel.SetBackgroundColour('#aaaaaa')
        sizer.Add(self.text6, (12, 1), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)
        
        self.tc6 = wx.TextCtrl(panel, -1,size=(150,30))
        sizer.Add(self.tc6, (12, 4), (1,7), wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        self.tc6.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL,wx.BOLD))

        b12=wx.Button(panel, -1, '  Plot Graph  ',pos=(530,400),size=(120,30))
        #sizer.Add(b12, (14,6), flag=wx.LEFT | wx.BOTTOM, border=10)
        self.Bind(wx.EVT_BUTTON,self.answer,id=b12.GetId())
        b12.SetFont(wx.Font(13, wx.SWISS, wx.NORMAL, wx.BOLD))

        b13=wx.Button(panel, -1, 'Insert box1',pos=(690,410),size=(120,20))
        #sizer.Add(b12, (14,6), flag=wx.LEFT | wx.BOTTOM, border=10)
        self.Bind(wx.EVT_BUTTON,self.answer3,id=b13.GetId())
        b13.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))

        b14=wx.Button(panel, -1, 'Insert box2',pos=(690,440),size=(120,20))
        #sizer.Add(b12, (14,6), flag=wx.LEFT | wx.BOTTOM, border=10)
        self.Bind(wx.EVT_BUTTON,self.answer4,id=b14.GetId())
        b14.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))
        
        self.Center()
        self.Show(True)

    def OnSelect3(self,event):
        item=event.GetSelection()
        self.k=item
        if item==3:
            self.text1.SetLabel('Enter the array of points in the format:[[x1,y1],[x2,y2],.....]') 
            self.text2.SetLabel('')
            self.text3.SetLabel('')
            self.text4.SetLabel('')
        if item==2:
            self.text1.SetLabel('Enter the array of points in the format:[[x1,y1],[x2,y2],.....]')
            self.text5.SetLabel('Enter the label for the first graph')
            self.text6.SetLabel('Enter the label for the Second graph')
            self.text2.SetLabel('g(x)=')
            self.text3.SetLabel('Enter the first number of your interval of x')
            self.text4.SetLabel('Enter the second number of your interval of x')
        if item==1:
            self.text1.SetLabel('f(x)=')
            self.text2.SetLabel('')
            self.text5.SetLabel('Enter the Y label')
            self.text6.SetLabel('Enter the X label')
            self.text3.SetLabel('Enter the first number of your interval of x')
            self.text4.SetLabel('Enter the second number of your interval of x')
        if item==0:
            self.text1.SetLabel('f(x)=')
            self.text2.SetLabel('g(x)=')
            self.text5.SetLabel('Enter the Y label')
            self.text6.SetLabel('Enter the X label')
            self.text3.SetLabel('Enter the first number of your interval of x')
            self.text4.SetLabel('Enter the second number of your interval of x')
        self.tc.SetValue('')
        self.tc2.SetValue('')
        self.tc3.SetValue('')
        self.tc4.SetValue('')
        self.tc5.SetValue('')
        self.tc6.SetValue('')
    
    def answer(self,event):
        text3=self.tc.GetValue()
        text4=self.tc2.GetValue()
        text5=self.tc3.GetValue()
        text6=self.tc4.GetValue()
        text7=self.tc5.GetValue()
        text8=self.tc6.GetValue()
        if self.k==3:
            b=self.conv(text3)
            lower=[None]*len(b)
            upper=[None]*len(b)
            for i in range(len(b)):
                lower[i]=b[i][0]
                upper[i]=b[i][1]
            graph.test(lower,upper,float(0),float(0),text8,text7,self.k)
        else:    
            graph.test(text3,text4,float(text5),float(text6),text8,text7,self.k)
        MyFrame(self,-1,'Graph Plotting')

    def conv(self,text):    
        k=0
        if text=='':
            return 0
        elif ord(text[0])-ord('0')<=9 and ord(text[0])-ord('0')>=0:
            return int(text)
        else:
            for i in range(len(text)):
                if (text[i]=='['):
                    k=k+1
            l=k
            if(k!=1):
                k=k-1
            lst=list()
            lst=text.split(',')
            print(len(lst))
            for i in range(len(lst)):
                if('[' in lst[i]):
                    lst[i]=lst[i].replace('[','')
                if(']' in lst[i]):
                    lst[i]=lst[i].replace(']','')
            m=k
            print lst 
            k=len(lst)/k
            print len(lst)
            if l!=1:
                b=[None]*m
                for i in range(m):
                    b[i]=[None]*(len(lst)/m)
                for i in range(len(lst)):
                    n=int(i/k)
                    m=i%k
                    print m,n
                    if lst[i]=='inf' or lst[i]=='+inf':
                        b[n][m]=300.0
                    elif lst[i]=='-inf':
                        b[n][m]=-300.0
                    else:
                        b[n][m]=float(lst[i])
                return b
            
            if l==1:
                b=[None]*len(lst)
                for i in range(len(lst)):
                    if lst[i]=='inf' or lst[i]=='+inf':
                        b[i]=300.0
                    elif lst[i]=='-inf':
                        b[i]=-300.0
                    else:
                        b[i]=float(lst[i])
                return b
            
    def answer3(self,event):
        sel=self.imp.GetSelection()
        text=self.imp.GetString(sel)
        self.tc.SetLabel(text)
        
    def answer4(self,event):
        sel=self.imp.GetSelection()
        text=self.imp.GetString(sel)
        self.tc2.SetLabel(text)
    
app = wx.App()
CAS(None, -1, 'Computerised Algebraic System')
app.MainLoop()




    
