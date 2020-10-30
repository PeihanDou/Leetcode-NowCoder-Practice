import functools

def cmp(x, y):
    if int(x+y) > int(y+x):
        return 1
    elif int(x+y) < int(y+x):
        return -1
    else: return 0

# 利用functools改变cmp的方法
# cmp 返回1则x>y，-1则x<y, 0则相等
def PrintMinNumber(numbers):
        # write code here
        numbers_str = list(map(str, numbers))
        numbers_str.sort(key = functools.cmp_to_key(cmp))
        return ''.join(numbers_str)

a = [19,32,31,3]
print(PrintMinNumber(a))