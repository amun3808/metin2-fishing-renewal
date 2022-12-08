# builtins
import event
import app
import wndMgr
import dbg
import player
# root modules
import ui
import uiScriptLocale
import math

class FishingGame(ui.ScriptWindow):
	FISHING_PATH = "d:/ymir work/ui/game/fishing/"
	FISH_PATH = FISHING_PATH + "fish/"
	WAVE_PATH = FISHING_PATH + "wave/"
	EFFECT_SIZE = 32 # Don't change this.

	# duration of "Miss", "Hit", and the wave
	EFFECT_DURATION = 0.3 # seconds

	# The amount of time required to wait before being able to hit the fish again
	HIT_WAIT = 1 # seconds
	# The amount of time penalized from the total time of the game when missing the fish
	MISS_PENALTY = 1 # seconds 

	# Fishing game duration
	FISHING_TIME_LIMIT = 15 # seconds
	# Number of hits required for a successful game
	HIT_TARGET_NUM = 3

	# the number of pixels traversed per frame
	# We can not traverse fractional pixels, so only use positive whole numbers(1,2,3,etc)
	FISH_SPEED = 2 # 1 - 2 seems great, higher goes a bit too fast

	# The speed at which the fish changes its direction(smaller = faster)
	FISH_CHANGE_DIRECTION_SPEED = 0.7 # 0.7 sec - 1 sec seems great

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__FullReset()

	def __del__(self):
		self.__FullReset()
		ui.ScriptWindow.__del__(self)

	def __FullReset(self):
		self.isLoaded = 0

		# # self.debugText_goal_pos_Local = None
		# self.debugText_fish_pos_Local = None
		# self.debugText_mouse_pos_Local = None
		# self.hitCount = None
		# self.timerBaseImage = None
		self.fishImage = None
		self.effectContainer = None
		self.waveEffect = None
		self.missEffect = None
		self.hitEffect = None
		self.backGroundWater = None
		self.goalCircle = None
		self.hitCountText = None
		self.timerGauge = None
		self.navigationArea = None
		self.board = None

		self.__Reset()

	def __Reset(self):
		self.endTime = 0
		self.clickTime = 0
		self.nextHit = 0
		self.nextCourse = 0
		self.courseX = 0
		self.courseY = 0
		self.hits = 0
		self.canHit = False
		if app.GetCursor() != app.NORMAL:
			app.SetCursor(app.NORMAL)

	def Destroy(self):
		self.ClearDictionary()
		self.__FullReset()
		self.Hide()

	def Close(self):
		self.HandleFishingPacket()
		self.__Reset()
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()

	def ClearFishing(self):
		pass

	def QuitFishing(self):
		self.__Reset()
		self.Hide()

	# only called by root when the time is up or when the fish got hit the required amount of times
	def HandleFishingPacket(self):
		player.QuitFishing(self.hits)
		self.QuitFishing()

	def StartFishing(self):
		self.__Reset()
		self.__Load()
		self.hitCountText.SetText("{}/{}".format(self.hits, self.HIT_TARGET_NUM))

		# Give the fish a random initial position
		self.ChangeCourse()
		self.fishImage.SetPosition(self.courseX, self.courseY)

		self.endTime = app.GetTime() + self.FISHING_TIME_LIMIT
		self.Show()

	def Show(self):
		self.__Load()
		ui.ScriptWindow.Show(self)

	def Open(self):
		self.Show()

	def __Load(self):
		if self.isLoaded:
			return

		self.isLoaded = 1

		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/FishingGameWindow.py")
		except:
			import exception
			exception.Abort("FishGame.__Load.UIScript/FishingGameWindow.py")

		try:
			self.board = self.GetChild('board')
			self.backGroundWater = self.GetChild('fishing_background_water')
			self.goalCircle = self.GetChild('fishing_goal_circle')
			self.hitCountText = self.GetChild('fishing_goal_count_text')
			self.timerGauge = self.GetChild('fishing_timer_gauge')
			self.navigationArea = self.GetChild('fishing_water_navArea')

			self.GetChild('debug_text_circle_pos').Hide()
			self.GetChild('debug_text_fish_pos').Hide()
			self.GetChild('debug_text_mouse_pos').Hide()
			self.GetChild('fishing_goal_count').Hide()
			self.GetChild('fishing_timer_baseImg').Hide()
		except:
			import exception
			exception.Abort("FishGame.__Load.BindObject")

		try:
			self.board.SetCloseEvent(ui.__mem_func__(self.Close))
			self.backGroundWater.SAFE_SetStringEvent("MOUSE_OVER_IN",self.OnMouseOverIn)
			self.backGroundWater.SAFE_SetStringEvent("MOUSE_OVER_OUT",self.OnMouseOverOut)
			self.backGroundWater.SAFE_SetStringEvent("MOUSE_BUTTON_DOWN", self.OnMouseLeftButtonDownEvent)
		except:
			import exception
			exception.Abort("FishGame.__Load.BindEvent")

		# @Amun: trick to get rid of overlapping: wrap the item in a container with size 0
		# This way the wave doesn't get in the way of registering the hover event for the board
		self.effectContainer = ui.ScriptWindow()
		self.effectContainer.SetParent(self.backGroundWater)
		self.effectContainer.SetSize(0,0)

		(cx, cy) = self.goalCircle.GetLocalPosition()
		(cw, ch) = (self.goalCircle.GetWidth(), self.goalCircle.GetHeight())

		# Set the effect container in the center of the circle(Origin point)
		self.effectContainer.SetPosition(cx + cw/2,cy + ch/2)
		self.effectContainer.Show()

		self.fishImage = ui.AniImageBox()
		self.fishImage.SetParent(self.effectContainer)
		self.fishImage.AppendImage(self.FISH_PATH + "fishing_fish_1.sub")
		self.fishImage.AppendImage(self.FISH_PATH + "fishing_fish_2.sub")
		self.fishImage.AppendImage(self.FISH_PATH + "fishing_fish_3.sub")
		self.fishImage.AppendImage(self.FISH_PATH + "fishing_fish_4.sub")
		self.fishImage.SetSize(self.EFFECT_SIZE, self.EFFECT_SIZE)
		self.fishImage.Show()

		self.waveEffect = ui.AniImageBox()
		self.waveEffect.SetParent(self.effectContainer)
		self.waveEffect.AppendImage(self.WAVE_PATH + "fishing_effect_wave_1.sub")
		self.waveEffect.AppendImage(self.WAVE_PATH + "fishing_effect_wave_2.sub")
		self.waveEffect.AppendImage(self.WAVE_PATH + "fishing_effect_wave_3.sub")
		self.waveEffect.AppendImage(self.WAVE_PATH + "fishing_effect_wave_4.sub")
		# self.waveEffect.SetSize(self.WAVE_SIZE,self.WAVE_SIZE)

		self.missEffect = ui.AniImageBox()
		self.missEffect.SetParent(self.effectContainer)
		self.missEffect.AppendImage(self.FISHING_PATH + "fishing_effect_miss.sub")

		self.hitEffect = ui.AniImageBox()
		self.hitEffect.SetParent(self.effectContainer)
		self.hitEffect.AppendImage(self.FISHING_PATH + "fishing_effect_hit.sub")

	def OnMouseLeftButtonDownEvent(self):
		self.clickTime = app.GetTime()

		fx, fy = self.fishImage.GetLocalPosition()
		fw, fh = self.fishImage.GetWidth(), self.fishImage.GetHeight()
		mx, my = wndMgr.GetMouseLocalPosition(self.effectContainer.hWnd)

		if ((mx >= fx) and (mx <= (fx + fw)) and ((my + 8) >= fy) and (my - 2 <= (fy + fh))):
			if (not self.canHit or (self.clickTime < self.nextHit)):
				return

			self.CreateHitEffect(mx, my - self.EFFECT_SIZE) # - size to raise it a little higher

			self.hits += 1
			self.hitCountText.SetText("{}/{}".format(self.hits, self.HIT_TARGET_NUM))

			self.nextHit = self.clickTime + self.HIT_WAIT #app.GetTime() + self.HIT_WAIT
		else:
			self.endTime = self.endTime - self.MISS_PENALTY
			self.timerGauge.SetDiffuseColor(1,0,0)
			self.CreateMissEffect(mx, my - self.EFFECT_SIZE) # - size to raise it a little higher

		self.CreateWaveEffect(mx - self.EFFECT_SIZE/2, my - self.EFFECT_SIZE/2, 10)

	def OnUpdate(self):
		appTime = app.GetTime()

		if appTime >= self.endTime or self.hits >= self.HIT_TARGET_NUM:
			self.HandleFishingPacket()

		if appTime >= self.nextCourse: # change course
			self.ChangeCourse()
			self.FISH_SPEED = app.GetRandom(1,2) # Remove if you don't like it
			self.nextCourse = appTime + self.FISH_CHANGE_DIRECTION_SPEED

	def OnRender(self):
		fx, fy = self.fishImage.GetLocalPosition()
		fw, fh = self.fishImage.GetWidth(), self.fishImage.GetHeight()

		nx = fx
		ny = fy

		# advance position if course != fish pos
		if self.courseX > (fx + self.FISH_SPEED):
			nx += self.FISH_SPEED
		elif self.courseX < (fx - self.FISH_SPEED):
			nx -= self.FISH_SPEED

		if self.courseY > (fy + self.FISH_SPEED):
			ny += self.FISH_SPEED
		elif self.courseY < (fy - self.FISH_SPEED):
			ny -= self.FISH_SPEED

		if nx != fx and ny != fy:# if the fish is stationary, skip
			radians = math.atan2(float(ny - fy), float(nx - fx))
			# deg = radians * 57.2957795131 + 90
			deg = radians * 180 / math.pi + 90 # (-180, 180)deg # +90deg to match image rotation
			self.fishImage.SetRotation(deg)
			self.fishImage.SetPosition(nx, ny)

			radius = self.goalCircle.GetWidth()/2
			if self.InRangeFromOrigin(radius, fx+fw/2, fy+fh/2):
				self.goalCircle.SetDiffuseColor(1,0,0)
				self.canHit = True
			else:
				self.goalCircle.SetDiffuseColor(1,1,1)
				self.canHit = False

		self.timerGauge.SetPercentage(max(0, self.endTime - app.GetTime()), self.FISHING_TIME_LIMIT)

		if app.GetTime() > (self.clickTime + self.EFFECT_DURATION):
			self.timerGauge.SetDiffuseColor(1,1,1)
			self.hitEffect.Hide()
			self.missEffect.Hide()
			self.waveEffect.Hide()


	# https://en.wikipedia.org/wiki/Euclidean_plane
	# https://en.wikipedia.org/wiki/Euclidean_distance
	def InRangeFromOrigin(self, radius, x, y):
		return ((x * x) + (y * y) < (radius * radius))

	def ChangeCourse(self):
		# Boundaries: (-nav/2, +nav/2)
		x = self.navigationArea.GetWidth()/2 - 10
		y = self.navigationArea.GetHeight()/2 - 10

		self.courseX = app.GetRandom(-x, x)
		self.courseY = app.GetRandom(-y, y)

	def CreateWaveEffect(self, x, y, delay = 0):
		self.waveEffect.SetDelay(delay)
		self.waveEffect.SetPosition(x,y)
		self.waveEffect.Show()

	def CreateMissEffect(self, x, y):
		self.missEffect.SetPosition(x, y)
		self.missEffect.Show()

	def CreateHitEffect(self, x, y):
		self.hitEffect.SetPosition(x, y)
		self.hitEffect.Show()

	def OnMouseOverOut(self):
		if app.GetCursor() != app.NORMAL:
			app.SetCursor(app.NORMAL)

	def OnMouseOverIn(self):
		if app.GetCursor() != app.FISH:
			app.SetCursor(app.FISH)
