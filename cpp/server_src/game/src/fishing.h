
find
extern void Take(fishing_event_info* info, LPCHARACTER ch);

add
#ifdef ENABLE_FISHING_RENEWAL
	extern void Stop(LPCHARACTER ch);
#endif
