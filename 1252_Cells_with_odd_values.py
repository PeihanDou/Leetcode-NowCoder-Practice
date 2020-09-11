##
##https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/
##

# 要分开看待indices[0]和[1]。
# 因为对indices[0]来说：
# 出现奇数次的行才会有奇数结果（除了那些被奇数列影响的部分）
# 对indices[1]相同
# 因此：
# 可以画图，奇数行和奇数列画线，行列有交点的是奇数加奇数的偶数。
# 算除去这些交点的有线经过的点即可！

import numpy as np

def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
    oddRow, oddCol = [False] * n, [False] * m
    cntRow, cntCol = 0, 0
    for r,c in indices:
        oddRow[r] ^= True
        oddCol[c] ^= True
        cntRow += 1 if oddRow[r] else -1
        cntCol += 1 if oddCol[c] else -1
    return (n - cntRow) * cntCol + (m - cntCol) * cntRow

