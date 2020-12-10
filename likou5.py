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
