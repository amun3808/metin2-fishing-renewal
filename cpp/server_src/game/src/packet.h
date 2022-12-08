change
typedef struct command_fishing
{
	uint8_t header;
	uint8_t dir;
#ifdef ENABLE_FISHING_RENEWAL
	uint8_t fgSuccess; // fishing game success or failure
#endif
} TPacketCGFishing;

