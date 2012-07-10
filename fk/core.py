import configurator
import wx
import mainWindow

def run():
	configurator.updateConfig()

	application = wx.App(False)
	frame = mainWindow.MainWindow(None, "Fennek")
	frame.Show(True)
	application.MainLoop()