def set_fun(func):
    print('set_fun')
    def call_fun(*args,**kwargs):
        print('call_fun')
        return func(*args,**kwargs)
    return call_fun

@set_fun # test = set_fun(test)  # 遇到语法糖，外部函数就执行了
def test(data):
    print("test is show%s"%str(data))

test(123)

@set_fun  # 一个装饰器装饰多个函数
def demo(data):
    print("show demo is %s"%str(data))

demo(1234)