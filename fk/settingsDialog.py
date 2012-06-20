import wx

class SettingsDialog(wx.Dialog):
	def __init__(self):
		wx.Dialog.__init__(self, None, wx.ID_ANY, "Settings")
		self.ShowModal()