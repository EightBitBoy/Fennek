import wx
from musicList import MusicList
from settingsDialog import SettingsDialog

class MainWindow(wx.Frame):
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, wx.ID_ANY ,title)

		fennekMenu = wx.Menu()
		settingsItem = fennekMenu.Append(wx.ID_EXIT, "Settings", "Fennek settings")
		self.Bind(wx.EVT_MENU, self.OnSelectSettingsItem, settingsItem)
		
		menuBar = wx.MenuBar()
		menuBar.Append(fennekMenu, "Fennek")
		self.SetMenuBar(menuBar)
		
		self.musicList = MusicList(self)
		
		self.Show(True)
	
	def OnSelectSettingsItem(self, e):
		SettingsDialog()