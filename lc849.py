##https://leetcode.com/problems/maximize-distance-to-closest-person/

##通过计算连续0的个数来决定坐在哪一组0的中间（或者坐在最两边）
n = int(input())
res = []
for i in range(n):
    stair = int(input())
    if stair == 1:
        print(0)
    else:
        f1, f2 = 0,1
        for s in range(stair):
            f1, f2 = f2, f1+f2
        res.append(str(f1))
print('\n'.join(res))