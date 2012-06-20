import wx
import mainWindow

def run():
    application = wx.App(False)
    frame = mainWindow.MainWindow(None, "Fennek")
    frame.Show(True)
    application.MainLoop()