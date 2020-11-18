'''
######好题#####
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007
'''

# 采用归并排序为基础
# 在判断两个序列时， 由于两个序列已经有序，且l的所有元素必定都在r所有元素之前，
# 那么如果l[0] > r[0] 说明有逆序对，而且有len(l)个
# 复杂度O(NlogN)
def InversePairs(data):
    # write code here
    res = [0]
    def merge_sort(arr, res):
        if len(arr) == 1: return arr
        mid = (len(arr))//2
        return merge(merge_sort(arr[:mid], res), merge_sort(arr[mid:], res), res)
    
    def merge(l, r, res):
        m = []
        while len(l) and len(r):
            if l[0] > r[0]:
                m.append(r.pop(0))
                res[-1] += len(l) # critical part
                res[-1] %= 1000000007
            else:
                m.append(l.pop(0))
        if l:
            m += l
        if r:
            m += r
        return m
    merge_sort(data, res)
    return res[-1]

