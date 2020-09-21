def longestValidParentheses(s):
    maxans = 0
    dp = [0] * len(s)
    for i in range(1, len(s)):
        if s[i] == ')' and s[i-1] == '(':
            dp[i] = 2 + (dp[i-2] if i >= 2 else 0)
        elif i-dp[i-1]-1 >= 0 and s[i] == ')' and s[i-1] == ')' and s[i-dp[i-1]-1] == '(':
            dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]
        maxans = max(maxans, dp[i])
    return maxans


##利用stack， 初始栈底为-1
##当s[i]是（时，push i 入栈。因为这时最大长度还不确定，不操作maxlen
##当s[i]是）时，pop一次。然后设置maxlen = i - stacktop的值
##pop之后，由于之前的有效序列肯定都弹出了，那么这时stacktop肯定是某个（对应的id
# 具体来说，stacktop会是 在目前的有效序列之前的一个（的id，那么i-stacktop就是新的有效序列的长度
# 如果s[i]是）的时候，stack空了，说明现在这个）之前的所有括号组成了一个有效序列，那么把这个）的id入栈，不操作maxlen
# 这之后就好比从i+1开始一个新序列，栈底是i （对比从i=0开始一个新序列，栈底是-1，保持了一致）
def longestValidParentheses1(s):
    stack = [-1]
    maxlen = 0
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        if s[i] == ')':
            stack.pop()
            if stack ==[]:
                stack.append(i)
            else:
                maxlen = max(maxlen, i - stack[-1])
    return maxlen

## 利用两个pointer
## 前提： 有效的序列必有l=r
## 前提2： 从左往右走的话，l<r的序列必然无效
def longestValidParentheses2(s):
        maxlen = 0
        l,r = 0,0
        for i in range(len(s)):
            if s[i] == '(':
                l += 1
            elif s[i] == ')':
                r += 1
            if l == r:
                maxlen = max(maxlen, 2*l)
            if l < r:
                l,r = 0,0
        l,r = 0,0
        for i in range(len(s)-1, -1, -1):
            if s[i] == '(':
                l += 1
            elif s[i] == ')':
                r += 1
            if l == r:
                maxlen = max(maxlen, 2*l)
            if l > r:
                l,r = 0,0
        return maxlen                