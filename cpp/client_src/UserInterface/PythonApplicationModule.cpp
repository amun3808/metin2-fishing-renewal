find
PyModule_AddIntConstant(poModule, "HVSIZE", CPythonApplication::CURSOR_SHAPE_HVSIZE);

add
#ifdef ENABLE_FISHING_RENEWAL
	PyModule_AddIntConstant(poModule, "FISH", CPythonApplication::CURSOR_SHAPE_FISH);
#endif

add this at the end, before }

#ifdef ENABLE_FISHING_RENEWAL
	PyModule_AddIntConstant(poModule, "ENABLE_FISHING_RENEWAL", 1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_FISHING_RENEWAL", 0);
#endif

