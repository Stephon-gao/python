def set_fun(func):

    def call_fun():
        print('权限')
        func()
    return call_fun

@set_fun # test = set_fun(test) 等号前的test只是个变量名而已，随便起都可以，
def test():  # 写test是为了让程序调用时不需要在调用处再改动
    print('test is show')

test() 

#结论: @set_fun ===> test = set_fun(test)
# test指向了set_fun的内部函数引用,func参数指向原先的test函数


# test = set_fun(test)
# test()
# test = set_fun(test)
# test()
#
# test()
#
# def test_s():
#     print("权限认证")
#     test()
#
# test_s()



