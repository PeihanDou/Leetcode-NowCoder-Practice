'''
A zero-indexed array A of length N contains all integers from 0 to N-1. 
Find and return the longest length of set S, 
where S[i] = {A[i], A[A[i]], A[A[A[i]]], ... } subjected to the rule below.

Suppose the first element in S starts with the selection of element A[i] of index = i, 
the next element in S should be A[A[i]], and then A[A[A[i]]]… By that analogy,
we stop adding right before a duplicate element occurs in S.


找出无重复数字的S[i] = {A[i], A[A[i]], A[A[A[i]]], ... }的最大长度
类似457
'''

def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_cnt = 0
        for i in range(len(nums)):
            mark = str(i)
            cnt = 0
            while type(nums[i]) == int:
                jump = nums[i]
                nums[i] = mark
                i = jump
                cnt += 1
                
            max_cnt = max(max_cnt, cnt)
        return max_cnt