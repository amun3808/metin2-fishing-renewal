find
	chrmgr.RegisterEffect(chrmgr.EFFECT_EMOTICON+11, "", EmoticonStr+"fish.mse")
	net.RegisterEmoticonString("(fish)")


add
	if app.ENABLE_FISHING_RENEWAL:
		chrmgr.RegisterEffect(chrmgr.EFFECT_EMOTICON+12, "", EmoticonStr+"fish_3.mse")
		net.RegisterEmoticonString("(fish2)")