import wx
import musicList
import settingsDialog

class MainWindow(wx.Frame):
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, wx.ID_ANY ,title)
		
		fennekMenu = wx.Menu()
		settingsItem = fennekMenu.Append(wx.ID_EXIT, "Settings", "Fennek settings")
		self.Bind(wx.EVT_MENU, self.showSettingsDialog, settingsItem)
		
		menuBar = wx.MenuBar()
		menuBar.Append(fennekMenu, "Fennek")
		self.SetMenuBar(menuBar)
		
		self.musicList = musicList.MusicList(self)
		
		self.Show(True)
	
	def showSettingsDialog(self, e):
		settingsWindow = settingsDialog.SettingsDialog()