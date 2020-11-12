'''
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。 例如
a & b & c & e
s & f & c & s
a & d & e & e
矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，
因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
'''


def hasPath(matrix, rows, cols, path):
        # write code here
        # dfs
        def dfs(i, j, pos, path):
            # 判断角标是否在matrix范围内
            if i<0 or i>=rows or j<0 or j>=cols:
                return False
            # 若已访问过 或者 不匹配，返回False
            if matrix[i][j] == "#" or matrix[i][j] != path[pos]:
                return False
                # 已经是最后一个字符，匹配成功
            if len(path) == pos+1:
                return True
            # 在matrix区域内，未访问过且匹配，且不是最后一个字符
            temp = matrix[i][j]
            matrix[i][j] = "#"
            if dfs(i-1, j, pos+1, path): return True
            if dfs(i, j-1, pos+1, path): return True
            if dfs(i+1, j, pos+1, path): return True
            if dfs(i, j+1, pos+1, path): return True
            matrix[i][j] = temp
            return False
        for i in range(rows):
            for j in range(cols):
                if dfs(i,j,0,path):
                    return True
        return False
