import wx
import musicList

class MainWindow(wx.Frame):
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, wx.ID_ANY ,title)
		
		fennekMenu = wx.Menu()
		fennekMenu.Append(wx.ID_EXIT, "Settings", "Fennek settings")
		menuBar = wx.MenuBar()
		menuBar.Append(fennekMenu, "Fennek")
		self.SetMenuBar(menuBar)
		
		self.musicList = musicList.MusicList(self)
		
		self.Show(True)