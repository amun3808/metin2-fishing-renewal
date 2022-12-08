IF you have PlayerSettingModule moved to source

find
rkNet.RegisterEmoticonString("(fish)");


add(or add it wherever you're loading the emoticons)

#ifdef ENABLE_FISHING_RENEWAL
	rkNet.RegisterEmoticonString("(fish2)");
#endif


same for this one, add it wherever you're registering the paths(might be in header file or something, idk)
#ifdef ENABLE_FISHING_RENEWAL
				{ CInstanceBase::EEffect::EFFECT_EMOTICON + 12, "", "d:/ymir work/effect/etc/emoticon/fish_3.mse" },
#endif
