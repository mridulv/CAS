import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (1000,700))

        self.bitmap = wx.Bitmap('example.png')
        wx.EVT_PAINT(self, self.OnPaint)

        self.Show(True)
        self.Centre()

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        dc.DrawBitmap(self.bitmap, 60, 20)





