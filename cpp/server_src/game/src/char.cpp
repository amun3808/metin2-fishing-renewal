find
void CHARACTER::fishing()

change
#ifdef ENABLE_FISHING_RENEWAL
void CHARACTER::fishing(uint8_t fg_success)
#else
void CHARACTER::fishing()
#endif


in that method, find 
fishing_take();

add before, like this
#ifdef ENABLE_FISHING_RENEWAL
		if (!fg_success)
		{
			fishing::Stop(this);
			event_cancel(&m_pkFishingEvent);
			return;
		}
#endif
		fishing_take();

