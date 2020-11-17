'''
给定两个字符串str1和str2,输出两个字符串的最长公共子串，如果最长公共子串为空，输出-1。
'''

'''
1.
求最长公共序列长度:
可以不连续，例如 loop和helloworld的最长公共序列是： loo
'''

def LCSequence(s1, s2):
    dp = [[0] * (len(s1)+1) for _ in range(len(s2)+1)]
    for i in range(len(s2) + 1):
        for j in range(len(s1) + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            else:
                if s1[j-1] == s2[i-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    return dp[-1][-1]

'''
2.
求最长公共子串长度
子串必须连续！
loop和helloworld的最长公共子串为lo
'''
def LCString(s1, s2):
    res = 0
    dp = [[0] * (len(s1)+1) for _ in range(len(s2)+1)]
    for i in range(len(s2) + 1):
        for j in range(len(s1) + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            else:
                if s1[j-1] == s2[i-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = 0
        res = max(res, max(dp[i]))
    return res

'''
如果想要输出最长公共子串结果而不是长度
'''

def LCS(str1 , str2 ):
        # write code here
        # 保证str1较短
        if len(str1) > len(str2):
            str1, str2 = str2, str1
        max_len, res = 0, ''
        for i in range(len(str1)):
            if str1[i-max_len: i+1] in str2:
                res = str1[i-max_len:i+1]
                max_len += 1
        if not res:
            return -1
        else:
            return res

# dp算法 O(n^2)
def LCS1(str1 , str2 ):
        # write code here
        start1 = 0
        res = 0
        if len(str1) > len(str2):
            str1, str2 = str2, str1
        dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

        
        for i in range(len(str1)+1):
            for j in range(len(str2)+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                else:
                    if str1[i-1] == str2[j-1]:
                        dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > res:
                    res = dp[i][j]
                    start1 = i  - res
        if res == 0: return -1
        return str1[start1:start1+res+1]


s1 = "123"
s2 = "1244123"
print(LCSequence(s1, s2))
print(LCString(s1,s2))
print(LCS1(s1,s2))

