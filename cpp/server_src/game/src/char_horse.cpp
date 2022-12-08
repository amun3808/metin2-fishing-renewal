in bool CHARACTER::StartRiding()

find
if (false == CHorseRider::StartRiding())
{
	...
}

add AFTER

#ifdef ENABLE_FISHING_RENEWAL
	if (m_pkFishingEvent)
		fishing(0,0);
#endif

or find
HorseSummon(false);

and add before