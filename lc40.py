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