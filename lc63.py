def uniquePathsWithObstacles(obstacleGrid):
        m,n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] != 1:
                    if i==0 and j==0:
                        dp[i][j] = 1
                    else:
                        left = dp[i-1][j] if i-1>=0 and obstacleGrid[i-1][j] != 1 else 0
                        upper = dp[i][j-1] if j-1>=0 and obstacleGrid[i][j-1] != 1 else 0
                        dp[i][j] = left + upper
        return dp[m-1][n-1]