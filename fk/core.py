import configurator
import database
import wx
import mainWindow


def run():
	configurator.updateConfig()

	# test some database stuff
	database.run()
	database.clearDatabase()
	database.fillDatabase()
	
	application = wx.App(False)
	frame = mainWindow.MainWindow(None, "Fennek")
	frame.Show(True)
	application.MainLoop()