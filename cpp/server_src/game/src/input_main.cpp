in void CInputMain::Fishing(LPCHARACTER ch, const char* c_pData)
find
ch->fishing();

replace
#ifdef ENABLE_FISHING_RENEWAL
	ch->fishing(p->fgSuccess);
#else
	ch->fishing();
#endif

