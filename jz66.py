'''
地上有一个m行和n列的方格。
一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。 
例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
'''

def movingCount(self, threshold, rows, cols):
        # write code here
        def check(n):
            s = 0
            while n:
                s += n%10
                n = n//10
            return s
        def dfs(i,j,si,sj, visited):
            # 若 出范围 或 数字和大于thresh 或 访问过
            if i>=rows or j >= cols or si+sj > threshold or (i,j) in visited:
                return 0
            # 访问标记
            visited.add((i,j))
            # 每访问一个格子就加一，并且访问右边的和下边的格子
            return 1+dfs(i+1, j, check(i+1), sj, visited) + dfs(i, j+1, si, check(j+1), visited)
        visited = set()
        return dfs(0,0,0,0, visited)

'''
不需要回溯，因为每一步只和上一步有关
对比65的回溯，那是由于65中这一步匹配失败后需要回退到这个格子未访问的状态
'''