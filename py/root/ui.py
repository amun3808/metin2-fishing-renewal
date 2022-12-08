in class AniImageBox(Window):
find 

	def RegisterWindow(self, layer):
		self.hWnd = wndMgr.RegisterAniImageBox(self, layer)

add

	def SetRotation(self, rotation):
		wndMgr.AniImageSetRotation(self.hWnd, rotation)



in class ImageBox(Window):

	def __init__(self, layer = "UI"):
		Window.__init__(self, layer)
make sure you have these
		self.eventDict = {}
		self.argDict = {}


find
	def SetAlpha(self, alpha):
		wndMgr.SetDiffuseColor(self.hWnd, 1.0, 1.0, 1.0, alpha)

if you don't have it, add

	def SetDiffuseColor(self, r, g, b, a = 1):
		wndMgr.SetDiffuseColor(self.hWnd, r, g, b, a)

then make sure you have these

	def OnMouseOverIn(self):
		try:
			apply(self.eventDict["MOUSE_OVER_IN"], self.argDict["MOUSE_OVER_IN"])
		except KeyError:
			pass

	def OnMouseOverOut(self):
		try:
			apply(self.eventDict["MOUSE_OVER_OUT"], self.argDict["MOUSE_OVER_OUT"])
		except KeyError:
			pass

	def OnMouseLeftButtonUp(self):
		try:
			apply(self.eventDict["MOUSE_CLICK"], self.argDict["MOUSE_CLICK"])
		except KeyError:
			pass

	def OnMouseLeftButtonDown(self):
		try:
			apply(self.eventDict["MOUSE_BUTTON_DOWN"], self.argDict["MOUSE_BUTTON_DOWN"])
		except KeyError:
			pass

	def SAFE_SetStringEvent(self, event, func, *args):
		self.eventDict[event] = __mem_func__(func)
		self.argDict[event] = args