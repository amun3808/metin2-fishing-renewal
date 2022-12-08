find
void initPlayer()

add before

#ifdef ENABLE_FISHING_RENEWAL
PyObject* playerQuitFishing(PyObject* poSelf, PyObject* poArgs)
{
	int iSuccess = 0;
	if (!PyTuple_GetInteger(poArgs, 0, &iSuccess))
		return Py_BadArgument();

	CPythonNetworkStream::Instance().SendFishingPacket(0, iSuccess);

	return Py_BuildNone();
}
#endif

find
				{ NULL,							NULL,								NULL },

or
		{ "IsSameItemVnum",				playerIsSameItemVnum,				METH_VARARGS },

add BEFORE
#ifdef ENABLE_FISHING_RENEWAL
		{ "QuitFishing",				playerQuitFishing,					METH_VARARGS },
#endif
