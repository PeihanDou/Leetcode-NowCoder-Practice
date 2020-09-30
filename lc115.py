# https://leetcode.com/problems/distinct-subsequences/

# dp[i][j] 代表s[:i]包含多少子序列等于t[:j]
# 那么对于一对i,j，如果s[i]!= t[j],则dp[i][j] = dp[i-1][j]，就是说
# 新增的s[i]对原本的s没有影响
# if s[i]==t[j], then dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
# 第一部分仍然是原本的s和t比较。第二部分意义是：假如新增的s[i]等于t[j]了,那么就不用判断s,t的最后一位，
# 而判断s[:i-1] and t[:j-1]即可，那么只要之前的序列s[i-1:]和t[:j-1]的dp值就可。
def numDistinct(self, s: str, t: str) -> int:
    dp = [[0] * (len(s)+1) for _ in range(len(t)+1)]
    for i in range(len(s)+1):
        dp[0][i] = 1
    for i in range(1, len(t)+1):
        for j in range(1, len(s)+1):
            dp[i][j] += dp[i][j-1]
            if t[i-1] == s[j-1]:
                dp[i][j] += dp[i-1][j-1]
    return dp[-1][-1]