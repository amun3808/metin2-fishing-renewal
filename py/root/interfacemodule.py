add
if app.ENABLE_FISHING_RENEWAL:
	import uiFishingGame

find
	def __MakeCubeResultWindow(self):
		self.wndCubeResult = uiCube.CubeResultWindow()
		self.wndCubeResult.LoadWindow()
		self.wndCubeResult.Hide()

add
	if app.ENABLE_FISHING_RENEWAL:
		def __MakeFishingGameWindow(self):
			self.wndFishingGame = uiFishingGame.FishingGame()
			self.wndFishingGame.Hide()

find
		self.__MakeCubeResultWindow()

add
		if app.ENABLE_FISHING_RENEWAL:
			self.__MakeFishingGameWindow()

find
		if self.wndCubeResult:
			self.wndCubeResult.Destroy()

add
		if app.ENABLE_FISHING_RENEWAL and self.wndFishingGame:
			self.wndFishingGame.Destroy()

find
		del self.wndCubeResult

add
		if app.ENABLE_FISHING_RENEWAL:
			del self.wndFishingGame

find
	#####################################################################################
	### Quest ###	
	def BINARY_ClearQuest(self, index):
		btn = self.__FindQuestButton(index)
		if 0 != btn:
			self.__DestroyQuestButton(btn)		

add before
	if app.ENABLE_FISHING_RENEWAL:
		def OpenFishingGameWindow(self):
			self.wndFishingGame.StartFishing()

		def CloseFishingGameWindow(self):
			self.wndFishingGame.QuitFishing()

