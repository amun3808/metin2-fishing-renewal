find
def OnFishingFailure(self):

replace
	def OnFishingFailure(self):
		chat.AppendChatWithDelay(chat.CHAT_TYPE_INFO, localeInfo.FISHING_FAILURE, 2000)


add
	if app.ENABLE_FISHING_RENEWAL:
		def OnFishingGameStart(self):
			self.interface.OpenFishingGameWindow()

		def OnFishingStopGame(self):
			self.interface.CloseFishingGameWindow()




