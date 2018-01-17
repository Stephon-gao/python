# 把中国的钱转换成外国的钱
# 汇率的值 * 钱 = 新钱

rate_usa = 0.7
money = 100
print(rate_usa * money)

rate_jp = 100
money = 2000
print(rate_jp * money)

# 一个函数做一件事(功能) -----函数,类的作用
# 类 方便相关函数管理
# 第一种方式,太烦了

def count_rate(rate,money):
    print(rate * money)

count_rate(100, 1000)
count_rate(0.7, 1000)

# 第二种常规的写法,太烦

def count_rate(money, rate = 0.7):
    print(money * rate)

count_rate(100)
count_rate(200)

count_rate(100,100)
count_rate(100,1000)
print("*"*90)

rate = 100
def count_rate(money):
    print(money * rate)

count_rate(100)

rate = 0.7
count_rate(100)

# 换汇率的时候 还是烦 我们再定义个类来做
class CountRate(object):
    def __init__(self, rate):
        self.rate = rate

    def __call__(self, money):
        print(self.rate * money)


rate_usa = CountRate(0.7)
rate_usa(100)  # 注：__init__方法的执行是由创建对象触发的,即:对象 = 类名();而对于 __call__ 方法的执行是由对象后加括号触发的，即：对象() 或者 类()()
rate_usa(200)
rate_jp = CountRate(1000)
rate_jp(1000)

rate_usa(300)

# 魔法方法 太多  ----只是计算这些小问题，还要定义个类，太麻烦了所以要用闭包。

print("*"* 100)
# 使用闭包
# 这个是干什么
# 这个怎么用
# 用在那里

#两个函数嵌套,外部函数返回内部函数的引用,并且外部函数都有参数（这就是闭包的写法）
# def 外部函数(args):
#     def 内部函数():
#         pass
#     return 内部函数引用

def count(rate):        # 闭包可以像类一样，保存一段值。
    def money(money):
        print(rate * money)
    return money


rate_usa = count(0.7)
rate_usa(100)

rate_jp = count(100)
rate_jp(100)

rate_usa(200)








