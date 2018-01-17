def test(data):
    print("test is show")

print(test)

test("123")

a = test

a(123)

print(a)


def application(func):
    func('123')

application(a)