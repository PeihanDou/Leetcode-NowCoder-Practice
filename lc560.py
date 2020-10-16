'''
Given an array of integers and an integer k,
you need to find the total number of continuous subarrays whose sum equals to k.
'''

'''
用dic记录出现过的sum，和出现的次数
同时检测sum - k在不在dic里面：
在的话，说明存在j 使得sum[i] - sum[j]=k，并且这个j有dic[sum[j]]个
'''
def subarraySum(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    dic = {0:1}
    s = 0
    cnt = 0
    for num in nums:
        s += num
        if s - k in dic:
            cnt += dic[s-k]
        dic[s] = dic.get(s, 0) + 1
    return cnt