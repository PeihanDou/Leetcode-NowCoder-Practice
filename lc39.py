# 找到所有组合，加起来等于target的组合
# candidates 里数字各不相同，combination可以重复利用candidates的数字
# dfs搜索
def combinationSum(candidates, target):
    def dfs(target, path):
        if target == 0:
            res.append(path)
            return 
        for i in candidates: #每次都重新遍历，因为数字可以重复利用，与lc40区分！
            if i > target:break
            if path and i < path[-1]: continue
            dfs(target-i, path+[i])
    res = []
    candidates = sorted(candidates)
    dfs(target, [])
    return res
