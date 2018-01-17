
def set_fun(func):
    def call_fun(data):
        print('权限认证')
        func(data)
    return call_fun

@set_fun # test = set_fun(test)
def test(data):
    print("test is show%s"%str(data))

test = set_fun(test)

test(1000)