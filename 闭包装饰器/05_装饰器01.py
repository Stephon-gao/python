
def set_fun(func):
	print("set_fun")
    def call_fun():
        print('权限认证')
        func()
    return call_fun

@set_fun # 等价test = set_fun(test)  # 此处会先执行set_fun函数，并返回call_fun对象
def test():  # 所以这个语法糖就表示，在 test函数后面该有 test = set_fun(test) 
    print("test is show")  # 这条语句的。注释掉的地方+test函数=语法糖+test函数。

# test = set_fun(test)

test()
# 结果为:
set_fun
权限认证
test is show
