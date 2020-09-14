##https://github.com/CyC2018/CS-Notes/blob/master/notes/17.%20%E6%89%93%E5%8D%B0%E4%BB%8E%201%20%E5%88%B0%E6%9C%80%E5%A4%A7%E7%9A%84%20n%20%E4%BD%8D%E6%95%B0.md


##输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数即 999。

def print1ToMaxOfNDigits(n):
    res = ['']
    ans = []
    while n > 0:
        res = combine(res)
        ans += res
        n -= 1
    return ans

def combine(l):
    new_l = []
    digits = [str(i) for i in range(10)]
    for i in l:
        for d in digits:
            if i != '0':
                new_l.append(i+d)
    return new_l
