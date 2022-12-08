find
		app.SetCursor(app.NORMAL)

add BEFORE
		if app.ENABLE_FISHING_RENEWAL:
			self.cursorDict[app.FISH] = CursorImage("D:/Ymir Work/UI/Cursor/fishing_mouse_cursor.sub")
			self.cursorPosDict[app.FISH] = (0, 0)
