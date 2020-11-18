'''
######好题########
把只包含质因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，因为它包含质因子7。 
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
'''

# 动态规划
# 维护三个指针，每次取min([res[p2]*2, res[p3]*3, res[p5]*5])作为新的值，而对应的p加一（乘p的紧接着大一点的数）
def GetUglyNumber_Solution(index):
    # write code here
    if index <= 0: return 0
    p2, p3, p5 = 0,0,0
    res = [0] * index
    res[0] = 1
    for i in range(1, len(res)):
        res[i] = min([res[p2]*2, res[p3]*3, res[p5]*5])
        if res[i] == res[p2]*2: p2 += 1
        if res[i] == res[p3]*3: p3 += 1
        if res[i] == res[p5]*5: p5 += 1
    return res[-1]
print(GetUglyNumber_Solution(8))