# 无参数,无返回值
# 无参数,有返回值
# 有参数,无返回值(指的是原函数的参数与返回值)
# 有参数,有返回值 (原函数要是有返回值，则内部函数也必须要return)
                # 也必须要有返回值。
def set_fun(func):
    # print("set_fun")
    def call_fun():
        print("call_fun") 
        func()
    return call_fun

@set_fun # test = set_fun(test)
def test():  # 无参无返回值
    print("test is show")

test()


##########################################

def set_fun(func):
    def call_fun():
         return func()  # 有返回值，func()接收test返回的123
    return call_fun  # 上一行不写return 结果打印为None

@set_fun # test = set_fun(test)
def test():  # 无参数，有返回值
    return 123  # 本身test()函数有返回值，内部函数必须要有返回值
                # 才能做到与原函数同步。
print(test())


###########################################
# 有参数,无返回值
# def set_fun(func):
#     def call_fun(data,*args,**kwargs):
#         func(data,*args,**kwargs)
#     return call_fun
#
# @set_fun
# def test(data,*args,**kwargs):
#     print(args)
#     print(kwargs)
#     print('show is %s'%str(data))
#
# test(9999)  # 结果为（在不同的行中）：()、 {}、 show is 9999
# test(9999,123, a= 123,b= 456)  
# 结果为：
# (123,)
# {'a': 123, 'b': 456}
# show is 9999


# 有参数,无返回值
def set_fun(func):
    def call_fun(*args,**kwargs):
        func(*args,**kwargs)
    return call_fun

@set_fun
def test(*args,**kwargs):  # 有参无返回值
    print(args)
    print(kwargs)

# test(9999)  结果为：(9999,) 、 {}
# test(9999,123, a= 123,b= 456)  结果为：(9999, 123)  、 {'b': 456, 'a': 123}
#######################################
有参数,有返回值

def set_fun(func):
    def call_fun(data):
        return func(data)
    return  call_fun

@set_fun
def test(data):
    return data

print(test(123))  # 结果为： 123

+++++++++++++++++++++++++++++++++++++++++++++++++
def set_fun(func):  # 这七行是一个通用的装饰器
    def call_fun(*args,**kwargs):  
        return func(*args,**kwargs)
    return  call_fun

@set_fun
def test():
    print("test is show")

test()

# @set_fun
# def test(*args,**kwargs):
#     return 123
#
# print(test(123))
