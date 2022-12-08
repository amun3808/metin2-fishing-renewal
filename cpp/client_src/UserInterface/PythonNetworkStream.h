find
bool SendFishingPacket(int iRotation);

replace
#ifdef ENABLE_FISHING_RENEWAL
	bool SendFishingPacket(int32_t iRotation, int32_t success = 0);
#else
	bool SendFishingPacket(int iRotation);
#endif
