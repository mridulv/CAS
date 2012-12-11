
import wx

class tictac(wx.Frame):
    def __init__(self,parent,id,title):
        wx.Frame.__init__(self,parent,id,title,size=(800,600))

        panel=wx.Panel(self,-1)
        self.k=1
        
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        fgs = wx.FlexGridSizer(4, 3, 9, 25)
        self.a=[[5,5,5],[5,5,5],[5,5,5]]
        
        t1=wx.StaticText(panel,-1,'')
        t2=wx.StaticText(panel,-1,'TIC TAC TOE')
        t2.SetFont(wx.Font(30, wx.SWISS, wx.NORMAL, wx.BOLD))
        t3=wx.StaticText(panel,-1,'')
        
        
        self.b1= wx.Button(panel, -1, '',size=(200,100))
        self.Bind(wx.EVT_BUTTON,self.window1,id=self.b1.GetId())
        self.b1.Bind(wx.EVT_RIGHT_DOWN,self.window2,id=self.b1.GetId())
        self.b1.SetFont(wx.Font(30, wx.SWISS, wx.NORMAL, wx.BOLD))
        
        self.b2= wx.Button(panel, -1, '',size=(200,100))
        self.Bind(wx.EVT_BUTTON,self.window3,id=self.b2.GetId())
        self.b2.Bind(wx.EVT_RIGHT_DOWN,self.window4,id=self.b2.GetId())
        self.b2.SetFont(wx.Font(30, wx.SWISS, wx.NORMAL, wx.BOLD))

        self.b3= wx.Button(panel, -1, '',size=(200,100))
        self.Bind(wx.EVT_BUTTON,self.window5,id=self.b3.GetId())
        self.b3.Bind(wx.EVT_RIGHT_DOWN,self.window6,id=self.b3.GetId())
        self.b3.SetFont(wx.Font(30, wx.SWISS, wx.NORMAL, wx.BOLD))

        self.b4= wx.Button(panel, -1, '',size=(200,100))
        self.Bind(wx.EVT_BUTTON,self.window7,id=self.b4.GetId())
        self.b4.Bind(wx.EVT_RIGHT_DOWN,self.window8,id=self.b4.GetId())
        self.b4.SetFont(wx.Font(30, wx.SWISS, wx.NORMAL, wx.BOLD))

        self.b5= wx.Button(panel, -1, '',size=(200,100))
        self.Bind(wx.EVT_BUTTON,self.window9,id=self.b5.GetId())
        self.b5.Bind(wx.EVT_RIGHT_DOWN,self.window10,id=self.b5.GetId())
        self.b5.SetFont(wx.Font(30, wx.SWISS, wx.NORMAL, wx.BOLD))

        self.b6= wx.Button(panel, -1, '',size=(200,100))
        self.Bind(wx.EVT_BUTTON,self.window11,id=self.b6.GetId())
        self.b6.Bind(wx.EVT_RIGHT_DOWN,self.window12,id=self.b6.GetId())
        self.b6.SetFont(wx.Font(30, wx.SWISS, wx.NORMAL, wx.BOLD))

        self.b7= wx.Button(panel, -1, '',size=(200,100))
        self.Bind(wx.EVT_BUTTON,self.window13,id=self.b7.GetId())
        self.b7.Bind(wx.EVT_RIGHT_DOWN,self.window14,id=self.b7.GetId())
        self.b7.SetFont(wx.Font(30, wx.SWISS, wx.NORMAL, wx.BOLD))

        self.b8= wx.Button(panel, -1, '',size=(200,100))
        self.Bind(wx.EVT_BUTTON,self.window15,id=self.b8.GetId())
        self.b8.Bind(wx.EVT_RIGHT_DOWN,self.window16,id=self.b8.GetId())
        self.b8.SetFont(wx.Font(30, wx.SWISS, wx.NORMAL, wx.BOLD))

        self.b9= wx.Button(panel, -1, '',size=(200,100))
        self.Bind(wx.EVT_BUTTON,self.window17,id=self.b9.GetId())
        self.b9.Bind(wx.EVT_RIGHT_DOWN,self.window18,id=self.b9.GetId())
        self.b9.SetFont(wx.Font(30, wx.SWISS, wx.NORMAL, wx.BOLD))
        
        fgs.AddMany([(t1,1,wx.EXPAND),(t2,1,wx.EXPAND),(t3,1,wx.EXPAND),(self.b1),(self.b2),(self.b3),(self.b4),(self.b5),(self.b6),(self.b7),(self.b8),(self.b9)])
        #fgs.AddGrowableRow(2,1)
        #fgs.AddGrowableCol(1,1)
        hbox.Add(fgs, 1, wx.ALL | wx.EXPAND, 15)
        panel.SetSizer(hbox)

        self.Centre()
        self.Show(True)

    def window1(self,event):
        if self.b1.GetLabel()=='' and self.k==1:
            self.k=0
            self.b1.SetLabel('x')
            self.a[0][0]=1
            i=self.call(self.a)
            if i==1:
                dial = wx.MessageDialog(None, 'Player X won', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
            if i==-1:
                dial = wx.MessageDialog(None, 'Player 0 won', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
            if i==2:
                dial = wx.MessageDialog(None, 'Match Drawn', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
    def window2(self,event):
        if self.b1.GetLabel()=='' and self.k==0:
            self.k=1
            self.b1.SetLabel('0')
            self.a[0][0]=0
            i=self.call(self.a)
            if i==1:
                dial = wx.MessageDialog(None, 'Player X won', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
            if i==-1:
                dial = wx.MessageDialog(None, 'Player 0 won', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
            if i==2:
                dial = wx.MessageDialog(None, 'Match Drawn', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
    def window3(self,event):
        if self.b2.GetLabel()=='' and self.k==1:
            self.k=0
            self.b2.SetLabel('x')
            self.a[0][1]=1
            i=self.call(self.a)
            if i==1:
                dial = wx.MessageDialog(None, 'Player X won', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
            if i==-1:
                dial = wx.MessageDialog(None, 'Player 0 won', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
            if i==2:
                dial = wx.MessageDialog(None, 'Match Drawn', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
    def window4(self,event):
        if self.b2.GetLabel()=='' and self.k==0:
            self.k=1
            self.b2.SetLabel('0')
            self.a[0][1]=0
            i=self.call(self.a)
            if i==1:
                dial = wx.MessageDialog(None, 'Player X won', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
            if i==-1:
                dial = wx.MessageDialog(None, 'Player 0 won', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
            if i==2:
                dial = wx.MessageDialog(None, 'Match Drawn', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
    def window5(self,event):
        if self.b3.GetLabel()=='' and self.k==1:
            self.k=0
            self.b3.SetLabel('x')
            self.a[0][2]=1
            i=self.call(self.a)
            if i==1:
                dial = wx.MessageDialog(None, 'Player X won', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
            if i==-1:
                dial = wx.MessageDialog(None, 'Player 0 won', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
            if i==2:
                dial = wx.MessageDialog(None, 'Match Drawn', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
    def window6(self,event):
        if self.b3.GetLabel()=='' and self.k==0:
            self.k=1
            self.b3.SetLabel('0')
            self.a[0][2]=0
            i=self.call(self.a)
            if i==1:
                dial = wx.MessageDialog(None, 'Player X won', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
            if i==-1:
                dial = wx.MessageDialog(None, 'Player 0 won', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
            if i==2:
                dial = wx.MessageDialog(None, 'Match Drawn', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
    def window7(self,event):
        if self.b4.GetLabel()=='' and self.k==1:
            self.k=0
            self.b4.SetLabel('x')
            self.a[1][0]=1
            i=self.call(self.a)
            if i==1:
                dial = wx.MessageDialog(None, 'Player X won', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
            if i==-1:
                dial = wx.MessageDialog(None, 'Player 0 won', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
            if i==2:
                dial = wx.MessageDialog(None, 'Match Drawn', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
    def window8(self,event):
        if self.b4.GetLabel()=='' and self.k==0:
            self.k=1
            self.b4.SetLabel('0')
            self.a[1][0]=0
            i=self.call(self.a)
            if i==1:
                dial = wx.MessageDialog(None, 'Player X won', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
            if i==-1:
                dial = wx.MessageDialog(None, 'Player 0 won', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
            if i==2:
                dial = wx.MessageDialog(None, 'Match Drawn', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
    def window9(self,event):
        if self.b5.GetLabel()=='' and self.k==1:
            self.k=0
            self.b5.SetLabel('x')
            self.a[1][1]=1
            i=self.call(self.a)
            if i==1:
                dial = wx.MessageDialog(None, 'Player X won', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
            if i==-1:
                dial = wx.MessageDialog(None, 'Player 0 won', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
            if i==2:
                dial = wx.MessageDialog(None, 'Match Drawn', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
    def window10(self,event):
        if self.b5.GetLabel()=='' and self.k==0:
            self.k=1
            self.b5.SetLabel('0')
            self.a[1][1]=0
            i=self.call(self.a)
            if i==1:
                dial = wx.MessageDialog(None, 'Player X won', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
            if i==-1:
                dial = wx.MessageDialog(None, 'Player 0 won', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
            if i==2:
                dial = wx.MessageDialog(None, 'Match Drawn', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
    def window11(self,event):
        if self.b6.GetLabel()=='' and self.k==1:
            self.k=0
            self.b6.SetLabel('x')
            self.a[1][2]=1
            i=self.call(self.a)
            if i==1:
                dial = wx.MessageDialog(None, 'Player X won', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
            if i==-1:
                dial = wx.MessageDialog(None, 'Player 0 won', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
            if i==2:
                dial = wx.MessageDialog(None, 'Match Drawn', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
    def window12(self,event):
        if self.b6.GetLabel()=='' and self.k==0:
            self.k=1
            self.b6.SetLabel('0')
            self.a[1][2]=0
            i=self.call(self.a)
            if i==1:
                dial = wx.MessageDialog(None, 'Player X won', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
            if i==-1:
                dial = wx.MessageDialog(None, 'Player 0 won', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
            if i==2:
                dial = wx.MessageDialog(None, 'Match Drawn', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
    def window13(self,event):
        if self.b7.GetLabel()=='' and self.k==1:
            self.k=0
            self.b7.SetLabel('x')
            self.a[2][0]=1
            i=self.call(self.a)
            if i==1:
                dial = wx.MessageDialog(None, 'Player X won', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
            if i==-1:
                dial = wx.MessageDialog(None, 'Player 0 won', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
            if i==2:
                dial = wx.MessageDialog(None, 'Match Drawn', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
    def window14(self,event):
        if self.b7.GetLabel()=='' and self.k==0:
            self.k=1
            self.b7.SetLabel('0')
            self.a[2][0]=0
            i=self.call(self.a)
            if i==1:
                dial = wx.MessageDialog(None, 'Player X won', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
            if i==-1:
                dial = wx.MessageDialog(None, 'Player 0 won', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
            if i==2:
                dial = wx.MessageDialog(None, 'Match Drawn', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
    def window15(self,event):
        if self.b8.GetLabel()=='' and self.k==1:
            self.k=0
            self.b8.SetLabel('x')
            self.a[2][1]=1
            i=self.call(self.a)
            if i==1:
                dial = wx.MessageDialog(None, 'Player X won', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
            if i==-1:
                dial = wx.MessageDialog(None, 'Player 0 won', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
            if i==2:
                dial = wx.MessageDialog(None, 'Match Drawn', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
    def window16(self,event):
        if self.b8.GetLabel()=='' and self.k==0:
            self.k=1
            self.b8.SetLabel('0')
            self.a[2][1]=0
            i=self.call(self.a)
            if i==1:
                dial = wx.MessageDialog(None, 'Player X won', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
            if i==-1:
                dial = wx.MessageDialog(None, 'Player 0 won', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
            if i==2:
                dial = wx.MessageDialog(None, 'Match Drawn', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
    def window17(self,event):
        if self.b9.GetLabel()=='' and self.k==1:
            self.k=0
            self.b9.SetLabel('x')
            self.a[2][2]=1
            i=self.call(self.a)
            if i==1:
                dial = wx.MessageDialog(None, 'Player X won', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
            if i==-1:
                dial = wx.MessageDialog(None, 'Player 0 won', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
            if i==2:
                dial = wx.MessageDialog(None, 'Match Drawn', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
    def window18(self,event):
        if self.b9.GetLabel()=='' and self.k==0:
            self.k=1
            self.b9.SetLabel('0')
            self.a[2][2]=0
            i=self.call(self.a)
            if i==1:
                dial = wx.MessageDialog(None, 'Player X won', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
            if i==-1:
                dial = wx.MessageDialog(None, 'Player 0 won', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
            if i==2:
                dial = wx.MessageDialog(None, 'Match Drawn', 'Exclamation', wx.OK |
                        wx.ICON_EXCLAMATION)
                dial.ShowModal()
                self.Close()
        

    def call(self,c):
        b=[0,0,0,0,0,0,0,0,0]
        for i in [0,1,2]:
            for j in [0,1,2]:
                b[8]=b[8]+c[i][j]
                if i+j==2:
                    b[7]=b[7]+c[i][j]
                if i==j:
                    b[6]=b[6]+c[i][i]
                b[i]=b[i]+c[j][i]
                b[i+3]=b[i+3]+c[i][j]
        for i in [0,1,2,3,4,5,6,7,8]:
            if b[i]==3:
                return 1
            elif b[i]==0:
                return -1
        if b[8]==5:
            return 2
        return 0


        
app = wx.App()
tictac(None, -1, 'CAS-:Computerised Algebraic System')
app.MainLoop()
        
        
        
