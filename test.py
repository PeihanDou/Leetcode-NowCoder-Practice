def dec(func):
    def pp():
        print("in pp")
        func()
    return pp


def func():
    print("in func")

@dec
def aa():
    print('aa')


print(aa())