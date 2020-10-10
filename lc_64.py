def minPathSum(self, grid):
    m,n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            if i==0 and j==0:
                dp[i][j] = grid[i][j]
            else:
                upper = dp[i-1][j] if i>0 else float('inf')
                left = dp[i][j-1] if j>0 else float('inf')
                dp[i][j] = min(upper, left) + grid[i][j]
    return dp[m-1][n-1]

# 和63很相似， 状态转移的方程不同
# 状态转移方程即dp[n] 和 dp[n-1], dp[n-2]的关系

# 用一维dp实现2维dp， 只能在二位dp只与左邻和上邻有关时能用
def minPathSum1(grid):
    m,n = len(grid), len(grid[0])
    dp = [0] * n
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                dp[j] = grid[0][0]
            elif i == 0:
                dp[j] = dp[j-1] + grid[i][j]
            elif j == 0:
                dp[j] = dp[j] + grid[i][j]
            else:
                dp[j] = min(dp[j], dp[j-1]) + grid[i][j]
    return dp[-1]
