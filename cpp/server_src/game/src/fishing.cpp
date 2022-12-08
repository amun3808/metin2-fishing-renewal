find
return (PASSES_PER_SEC(6));

replace
#ifdef ENABLE_FISHING_RENEWAL
			return (PASSES_PER_SEC(15));
#else
			return (PASSES_PER_SEC(6));
#endif

find
		int time = number(10, 40);
		return event_create(fishing_event, info, PASSES_PER_SEC(time));

replace
#ifdef ENABLE_FISHING_RENEWAL
		return event_create(fishing_event, info, PASSES_PER_SEC(0));
#else
		int time = number(10, 40);
		return event_create(fishing_event, info, PASSES_PER_SEC(time));
#endif


find

		if (ms > 6000)
			return -1;
		int time_step = MINMAX(0, ((ms + 99) / 200), MAX_FISHING_TIME_COUNT - 1);

replace

#ifdef ENABLE_FISHING_RENEWAL
		if (ms > 15000)
			return -1;
		int time_step = MINMAX(0, ((ms + 99) / 500), MAX_FISHING_TIME_COUNT - 1);
#else
		if (ms > 6000)
			return -1;
		int time_step = MINMAX(0, ((ms + 99) / 200), MAX_FISHING_TIME_COUNT - 1);
#endif

find
void Take(fishing_event_info* info, LPCHARACTER ch)

add before
#ifdef ENABLE_FISHING_RENEWAL
	void Stop(LPCHARACTER ch)
	{
		TPacketGCFishing p;
		p.header = HEADER_GC_FISHING;
		p.subheader = FISHING_SUBHEADER_GC_STOP;
		p.info = ch->GetVID();
		ch->PacketAround(&p, sizeof(p));
	}
#endif
