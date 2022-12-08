find
	void			fishing();
	void			fishing_take();

replace

	// FISING
#ifdef ENABLE_FISHING_RENEWAL
	void			fishing(uint32_t conf_key, uint8_t fg_success);
	void			fishing_take(uint32_t conf_key);
#else
	void			fishing();
	void			fishing_take();
#endif
	// END_OF_FISHING
