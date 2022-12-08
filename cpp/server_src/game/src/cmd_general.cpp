find
ch->fishing();

replace
#ifdef ENABLE_FISHING_RENEWAL
	ch->fishing(0,0);
#else
	ch->fishing();
#endif