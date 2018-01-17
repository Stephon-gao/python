class Func(object):
    def __init__(self,func):
        self.func = func

    def __call__(self):
        print("权限认证")
        self.func()


@Func  # test = Func(test)
def test():
    print("test is show")

test()