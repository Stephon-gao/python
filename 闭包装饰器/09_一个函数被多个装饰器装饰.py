def set_fun1(func):
    print('func1')
    def call_fun():
        print('call_fun1')
        func()
    return call_fun


def set_fun2(func):
    print('func2')
    def call_fun():
        print('call_fun2')
        func()
    return call_fun

@set_fun1
@set_fun2
def test():
    print('test is show')

test() 
# 结果为
# func2
# func1
# call_fun1
# call_fun2
# test is show