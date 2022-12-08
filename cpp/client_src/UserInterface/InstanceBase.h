find
EMOTICON_FISH = 11,

add
#ifdef ENABLE_FISHING_RENEWAL
		EMOTICON_FISH_FAIL = 12, // @Amun: This has to match playersettingmodule
#endif

find
void SetFishEmoticon();

add
#ifdef ENABLE_FISHING_RENEWAL
	void SetFishingFailEmoticon();
#endif
