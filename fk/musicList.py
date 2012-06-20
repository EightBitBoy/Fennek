import wx

class MusicList(wx.ListView):
	def __init__(self, parent):
		wx.ListView.__init__(self, parent)
		
		self.InsertColumn(0, "Location")
		
		item = wx.ListItem()
		item.SetText("foo")
		self.InsertItem(item)