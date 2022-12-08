find

bool CPythonNetworkStream::SendFishingPacket(int iRotation)
{
	uint8_t byHeader = HEADER_CG_FISHING;
	if (!Send(sizeof(byHeader), &byHeader))
		return false;
	uint8_t byPacketRotation = iRotation / 5;
	if (!Send(sizeof(uint8_t), &byPacketRotation))
		return false;

	return true;
}

replace with

#ifdef ENABLE_FISHING_RENEWAL
bool CPythonNetworkStream::SendFishingPacket(int32_t iRotation, int32_t success)
{
	TPacketCGFishing pack{};
	pack.header = HEADER_CG_FISHING;
	pack.dir = iRotation / 5;
	pack.fgSuccess = success;

	if (!Send(sizeof(TPacketCGFishing), &pack))
		return false;

	return true;
}
#else
bool CPythonNetworkStream::SendFishingPacket(int iRotation)
{
	uint8_t byHeader = HEADER_CG_FISHING;
	if (!Send(sizeof(byHeader), &byHeader))
		return false;
	uint8_t byPacketRotation = iRotation / 5;
	if (!Send(sizeof(uint8_t), &byPacketRotation))
		return false;

	return true;
}
#endif


modify
	case FISHING_SUBHEADER_GC_START:
		pFishingInstance->StartFishing(float(FishingPacket.dir) * 5.0f);
#ifdef ENABLE_FISHING_RENEWAL
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "OnFishingGameStart", Py_BuildValue("()"));
#endif
		break;

modify

	case FISHING_SUBHEADER_GC_STOP:
#ifdef ENABLE_FISHING_RENEWAL
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "OnFishingStopGame", Py_BuildValue("()"));
#endif
		if (pFishingInstance->IsFishing())
		{
			pFishingInstance->StopFishing();
		}
		break;

modify

	case FISHING_SUBHEADER_GC_REACT:
#ifndef ENABLE_FISHING_RENEWAL
		if (pFishingInstance->IsFishing())
		{
			pFishingInstance->SetFishEmoticon(); // Fish Emoticon
			pFishingInstance->ReactFishing();
		}
#endif
		break;

modify

	case FISHING_SUBHEADER_GC_SUCCESS:
#ifdef ENABLE_FISHING_RENEWAL
		pFishingInstance->SetFishEmoticon(); // Fishing success Emoticon
#endif
		pFishingInstance->CatchSuccess();
		break;

modify

	case FISHING_SUBHEADER_GC_FAIL:
#ifdef ENABLE_FISHING_RENEWAL
		pFishingInstance->SetFishingFailEmoticon(); // Fishing fail(empty hook) Emoticon
#endif
		pFishingInstance->CatchFail();
		if (pFishingInstance == CPythonCharacterManager::Instance().GetMainInstancePtr())
		{
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "OnFishingFailure", Py_BuildValue("()"));
		}
		break;

