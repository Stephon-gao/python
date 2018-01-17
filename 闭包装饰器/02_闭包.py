def set_fun(func):  # 有参数的闭包
    def call_fun():
        pass
    return call_fun


def set_fun():  # 没有参数的闭包,就等于下面两个函数的组合,就失去了闭包的意义了,
    def call_fun():  # 还不如不写闭包呢，所以参数一定要加上才有意义。
        pass
    return call_fun


def call_fun():
    pass


def set_fun():
    return call_fun

# set_fun()  == > call_fun()