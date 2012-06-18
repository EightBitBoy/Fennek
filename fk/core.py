import wx

def run():
    application = wx.App(False)
    frame = wx.Frame(None, wx.ID_ANY, "Hello World!")
    frame.Show(True)
    application.MainLoop()