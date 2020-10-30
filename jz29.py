
'''
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4
'''
# 快速排序，更改终止条件
def GetLeastNumbers_Solution(tinput, k):
        # write code here
        def patition(arr, l, r):
            pivot = arr[r-1]
            i = l
            for j in range(l, r-1):
                if arr[j] < pivot:
                    tinput[i], tinput[j] = tinput[j], tinput[i]
                    i += 1
            tinput[i], tinput[r-1] = tinput[r-1], tinput[i]
            return i
        l,r = 0, len(tinput)
        if k==0 or len(tinput) < k: return []
        while l < r:
            p = patition(tinput, l, r)
            if p+1 == k:
                return tinput[:k]
            elif p+1 < k:
                l = p+1
            elif p+1 > k:
                r = p
        return []
a = [5,2,4,1,3,6,3,7]
print(GetLeastNumbers_Solution(a, 4))

