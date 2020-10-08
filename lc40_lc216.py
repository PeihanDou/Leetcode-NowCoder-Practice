# 找到所有组合，加起来等于target的组合
# candidates 里数字可能重复，combination一个数字只能用一次
# dfs搜索
def combinationSum2(candidates, target):
    used_index = set()
    res = []
    
    def dfs(target, path, start):
        if target == 0:
            if path not in res:    
                res.append(path)
            return
        for i in range(start, len(candidates)): # 每次从start的地方开始遍历，并忽略连续的相同数字，因为一个数字只能用一次
            if candidates[i] > target:
                break
            if i > start and candidates[i] == candidates[i-1] : # 忽略连续的相同数字，因为一个数字只能用一次
                continue
            if i not in used_index:
                used_index.add(i)
                dfs(target - candidates[i], path+[candidates[i]], i+1)
                used_index.remove(i)
                
    candidates = sorted(candidates)
    dfs(target, [], 0)
    return res

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