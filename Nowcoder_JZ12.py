##利用递归使算法复杂度变为O（logN）
##利用abs简化helper的情况

def Power( base, exponent):
        # write code here
        if exponent == 0:return 1
        if base == 0: return 0
        res = 1
        res = res * helper(base, abs(exponent))
        return res if exponent > 0 else 1/res
        
def helper(base, exponent):
    if exponent == 0:
        return 1
    if exponent % 2 == 0:
        return helper(base*base, exponent//2)
    else:
        return base * helper(base*base, (exponent-1)//2)

print(Power(2,-3))