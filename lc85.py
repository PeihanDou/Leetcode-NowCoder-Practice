## 类似84题：在直方图中找到最大的矩形
## 只要将matrix每一行转换成直方图即可
def maximalRectangle(matrix):
    if not matrix: return 0
    m,n = len(matrix), len(matrix[0])
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == "1":
                matrix[i][j] = int(matrix[i][j]) + int(matrix[i-1][j] if i>0 else 0)
            else:
                matrix[i][j] = 0
    
    # 这是输入直方图，返回直方图里最大矩形的算法，利用单调栈
    # 在遍历h的时候，如果有更高的h[i]，则存储i入栈
    # 下一个h与栈顶比较，如果更高则id进展，否则就把stack里目前最高的柱子作为高，i和直到上一个比它矮的柱子的坐标差作为宽。
    # 保存最大值
    def maxRecHistgram(height):
        if not height: return 0
        height.append(0)
        stack = [-1]
        maxarea = 0
        for i in range(len(height)):
            while (height[i] < height[stack[-1]]):
                h = height[stack.pop()]
                w = i - 1 - stack[-1]
                maxarea = max(maxarea, h*w)
            stack.append(i)
        return maxarea
    
    
    maxRec = 0
    for row in matrix:
        maxRec = max(maxRec, maxRecHistgram(row))
    return maxRec