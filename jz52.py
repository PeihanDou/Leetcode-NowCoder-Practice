'''
############好题， 多看看#########
请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。 
在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
'''

# 2D dp
# 三种情况
# 1. s[j-1] p[i-1] 都是正常字符或.   dp[i][j] = dp[i-1][j-1] and (s[j-1] == p[i-1] or p[i-1] == ".")
# 2. p[i-1] 是 "*"重复0次: 那么p[i-2]p[i-1]可以视为没有，dp[i][j] = dp[i-2][j]
# 3. p[i-1] 是 "*"重复多次: 那么s[j-1可以视为没有（被*吸收掉）, dp[i][j] = dp[i][j-1]
# 注意2和3的对dp操作需要用or逻辑合并
def match(self, s, p):
    # write code here
    dp = [[0] * (len(s)+1) for _ in range(len(p)+1)]
    dp[0][0] = 1
    for i in range(1, len(p)+1):
        # 如果p是空字符串，则不匹配任何空字符串
        for j in range(len(s)+1):
            if p[i-1] != "*":
                if j > 0 and (s[j-1]==p[i-1] or p[i-1] == "."):
                    dp[i][j] = dp[i-1][j-1]
            else: # has *
                if i>=2: # repeat 0 time
                    dp[i][j] = dp[i-2][j]
                if i>=2 and j>=1 and (s[j-1] == p[i-2] or p[i-2] == "."): # 注意条件， i要大于2（因为*前必有一个数），j要大于1（非空）
                    dp[i][j] |= dp[i][j-1]
    return dp[-1][-1]