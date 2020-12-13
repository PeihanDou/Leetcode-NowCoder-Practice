# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

def longestPalindrome(s):
        dp = [[False] * len(s) for _ in range(len(s))]
        ans = ""
        for j in range(len(s)):
            for i in range(j, -1, -1):
                if i == j:
                    dp[i][j] = True
                elif i == j - 1:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
                if dp[i][j] and j-i+1 > len(ans):
                    ans = s[i:j+1]
        print(dp)
        return ans

def longestPalindrome1(s):
    def expand(s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return l+1, r-1
    if len(s) <= 1: return s
    l, r = 0, 0
    for i in range(len(s)-1):
        l1, r1 = expand(s, i, i)
        l2, r2 = expand(s, i, i+1)
        if r1 - l1 > r2 - l2 and r1 - l1 > r - l:
            l, r = l1, r1
        if r2 - l2 > r1 - l1 and r2 - l2 > r -l:
            l, r = l2, r2
    return s[l:r+1]
