find 
void initwndMgr()

add before
PyObject* wndAniImageSetRotation(PyObject* poSelf, PyObject* poArgs)
{
	UI::CWindow* pWindow;
	if (!PyTuple_GetWindow(poArgs, 0, &pWindow))
		return Py_BuildException();
	float fRotation;
	if (!PyTuple_GetFloat(poArgs, 1, &fRotation))
		return Py_BuildException();

	((UI::CAniImageBox*)pWindow)->SetRotation(fRotation);

	return Py_BuildNone();
}

find
		{ "AppendImage",				wndImageAppendImage,				METH_VARARGS },

add
		{ "AniImageSetRotation",		wndAniImageSetRotation,				METH_VARARGS },
