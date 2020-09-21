## best explaination ever! should read more times
## https://leetcode.com/problems/edit-distance/discuss/159295/Python-solutions-and-intuition

##递归的方法，用了cache，即用了可回溯的字典
def minDistance2(word1, word2, i, j, memo):
    """Memoized solution"""
    if i == len(word1) and j == len(word2):
        return 0
    if i == len(word1):
        return len(word2) - j
    if j == len(word2):
        return len(word1) - i

    if (i, j) not in memo:
        if word1[i] == word2[j]:
            ans = minDistance2(word1, word2, i + 1, j + 1, memo)
        else: 
            insert = 1 + minDistance2(word1, word2, i, j + 1, memo)
            delete = 1 + minDistance2(word1, word2, i + 1, j, memo)
            replace = 1 + minDistance2(word1, word2, i + 1, j + 1, memo)
            ans = min(insert, delete, replace)
        memo[(i, j)] = ans
    return memo[(i, j)]


## 对比递归，dp就是提前把回溯的字典扩充为包含所有情况的字典。
# 然后针对初始值进行初始化（需要谨慎思考确定初始化的是什么）
# 之后在遍历dp的时候就可以理解为递归的不同阶段，这时只要对比递归时的函数调用情况，就可以较容易地写出状态转移方程
# 虽然有时直接以dp思考更文直观一些
# 但是可以认为递归是dp的基础

def minDistance(word1, word2):
        m, n = len(word1), len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        return dp[m][n]