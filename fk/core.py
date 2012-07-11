import configurator
import database
import wx
import mainWindow


def run():
	configurator.updateConfig()
	database.run()
	
	application = wx.App(False)
	frame = mainWindow.MainWindow(None, "Fennek")
	frame.Show(True)
	application.MainLoop()