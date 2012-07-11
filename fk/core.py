import configurator
import database
import wx
import mainWindow


def run():
	configurator.updateConfig()

	# test some database stuff
	database.checkDatabase()
	#database.clear()
	#database.fill()
	
	application = wx.App(False)
	frame = mainWindow.MainWindow(None, "Fennek")
	frame.Show(True)
	application.MainLoop()