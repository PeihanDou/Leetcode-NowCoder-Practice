'''
Given an array of n positive integers and a positive integer s, 
find the minimal length of a contiguous subarray of which the sum ≥ s. 
If there isn't one, return 0 instead.
'''
def minSubArrayLen(s, nums):
    left = 0
    min_sub = float('inf')
    sub_sum = 0
    for i in range(len(nums)):
        sub_sum += nums[i]
        while sub_sum >= s:
            min_sub = min(min_sub, i+1-left)
            sub_sum -= nums[left]
            left += 1
    return min_sub if min_sub != float('inf') else 0