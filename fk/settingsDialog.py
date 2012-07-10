import wx

class SettingsDialog(wx.Dialog):
	def __init__(self):
		wx.Dialog.__init__(self, None, wx.ID_ANY, "Settings")
		
		#panel = wx.Panel(self)
		
		okButton = wx.Button(self, label="OK")
		okButton.Bind(wx.EVT_BUTTON, self.onClose)
		
		self.ShowModal()	
	def onClose(self, e):
		self.Destroy()