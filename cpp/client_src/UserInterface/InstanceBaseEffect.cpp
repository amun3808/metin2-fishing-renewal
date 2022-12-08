find
void CInstanceBase::SetFishEmoticon()
{
	SetEmoticon(EMOTICON_FISH);
}

add
#ifdef ENABLE_FISHING_RENEWAL
void CInstanceBase::SetFishingFailEmoticon()
{
	SetEmoticon(EMOTICON_FISH_FAIL);
}
#endif
