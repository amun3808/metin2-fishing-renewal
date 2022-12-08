find
void	EndEmotionProcess();

add
#ifdef ENABLE_FISHING_RENEWAL
	void SetFishingGameConfirmationKey(uint32_t key)
	{
		m_fishingConfirmationKey = key;
	}

	uint32_t GetFishingGameConfirmationKey() const
	{
		return m_fishingConfirmationKey;
	}
#endif

find
private:
	std::map<uint32_t, uint32_t> m_kMap_dwAffectIndexToSkillIndex;

add like this
private:
#ifdef ENABLE_FISHING_RENEWAL
	uint32_t				m_fishingConfirmationKey{0};
#endif
	std::map<uint32_t, uint32_t> m_kMap_dwAffectIndexToSkillIndex;

