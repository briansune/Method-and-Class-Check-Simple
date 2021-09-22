import TestMod

o_test_mod = TestMod.MyClass()


def pass_method(o_class2call, s_module, params):
    test_method = callable(getattr(o_class2call, s_module, None))
    print 'Method to be tested are: {}'.format(test_method)
    if not test_method:
        print 'Method does not exist'
        return

    o_method_try_call = getattr(o_class2call, s_module)

    print o_class2call.__class__
    print o_class2call.__module__
    print o_method_try_call.__name__
    o_class2call.test_b = params
    print o_method_try_call()


pass_method(o_test_mod, 'my_test', False)
pass_method(o_test_mod, 'get_bool', False)
