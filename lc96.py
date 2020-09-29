#对于dp[i],第i个节点可以做根，dp[i-1]种，可以做叶子，dp[i-1]种
#做中间结点时，上下两个树也是BTS，所以根据中间点所在的位置j(j会把除去第i个节点的i-1个节点分为两个树)，有dp[j] * dp[i-1-j]种分配

def numTrees(n):
    if n <= 1: return n
    dp = [0] * (n+1)
    dp[0],dp[1] = 0,1
    for i in range(2,n+1):
        inter_num = 0
        for j in range(i):
            inter_num += dp[j]*dp[i-1-j]
        dp[i] = dp[i-1] * 2 + inter_num
    return dp[-1]

# improvement：加入新节点在第i个位置上，那么分为dp[i-1]（该节点之上的树）和dp[n-i+1]（以该节点为根的树）
def numTrees1(n):
    if n <= 1: return n
    dp = [0] * (n+1)
    dp[0],dp[1] = 1,1
    for i in range(2,n+1):
        for j in range(0,i):
            dp[i] += dp[j]*dp[i-j-1]
    return dp[-1]