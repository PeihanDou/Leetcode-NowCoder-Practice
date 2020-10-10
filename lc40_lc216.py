# 找到所有组合，加起来等于target的组合
# candidates 里数字可能重复，combination一个数字只能用一次
# dfs搜索
def combinationSum2(candidates, target):
    def combine_sum_2(nums, start, path, result, target):
        if not target:
            result.append(path)
            return
        
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]: # 只有i大于start的时候才判断这个，因为i不大于start的话，认为是candidate里的新的一个数字
            ## 例如[2,2,2], i = start = 0,过这个判断，进下一层（下一层就是[2,2]了！）
            ## 但是回来的时候， i=1 > start，这时才判断是重复的（因为之前的递归已经把重复的数字用掉了）
                continue
            if nums[i] > target:
                break
            combine_sum_2(nums, i + 1, path + [nums[i]], 
                               result, target - nums[i])

    # Sorting is really helpful, se we can avoid over counting easily
    candidates.sort()                      
    result = []
    combine_sum_2(candidates, 0, [], result, target)
    return result
    
    
'''
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

'''

# dfs，终止条件：k<0 or target <0:已经用尽了k个数，或者目前的几个数之和已经超过target
# 终止条件： k=0 and target = 0：用了k个数，和为target，记录path
# 不满足终止条件时， k>0 or target > 0:在剩余的nums里选一个数，调用下一层dfs
# 你妈的，为啥我就想不到如此优雅的方法。我操了！
def combinationSum3(k, n):
    def dfs(target, nums, k, path):
        if k < 0 or target < 0:
            return
        if k==0 and target==0:
            ret.append(path)
        for i in range(len(nums)):
            dfs(target - nums[i], nums[i+1:], k-1, path+[nums[i]])
            
    ret = []
    dfs(n, range(1,10), k, [])
    return ret