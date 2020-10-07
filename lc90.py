# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

# 大方向：遍历nums，把每一个新的数字加到res的每个subset里，在加入res
# 例外： num[i] == nums[i-1]时，不要修改res的每一个subset，而是只修改res的最后l个subset（由于nums[i-1]而新增的那些subset）
def subsetsWithDup(nums):
        res = [[]]
        nums.sort()
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                l = len(res)
            for j in range(len(res)-l, len(res)):
                res.append(res[j] + [nums[i]])
        return res