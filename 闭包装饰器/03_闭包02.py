# a = 300  # 全局变量
def set_fun(func):

    # a = 100
    def call_fun():

        # nonlocal a  # 想要使用外部函数的变量，要加 nonlocal;全局变量当然在哪都能使用，但是修改要global。
        print(a)  # 上一行注释了，找不到变量a，此行出错；若在本内部函数中先定义一个变量a，此行就正确。

        b = 200  # 若此处是a = 200,上面一行也会报错，因为在后面定义变量a没有卵用.
    return call_fun


fun = set_fun(123)
fun()


