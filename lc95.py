# 思路
# 用dfs生成所有可能性
# 在[0,n-1]上循环，每一个点做根有多少结构？
# 假设i做根，那么左树的所有可能性为dfs[0,i-1]，右树为dfs[i+1,n-1]
# 注意终止条件，即可。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def generateTrees(n):
    def genTree(l, r):
        if l==r:
            return [None]
        nodes = []
        for i in range(l,r):
            for lchild in genTree(l,i):
                for rchild in genTree(i+1,r):
                    node = TreeNode(i+1)
                    node.left = lchild
                    node.right = rchild
                    nodes.append(node)
        return nodes
    return genTree(0, n) if n else []