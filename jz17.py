'''输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）'''

# 遍历r1，判断每个节点为根节点的树是否包含r2

def HasSubtree(pRoot1, pRoot2):
        if not pRoot1 or not pRoot2: return False
        return dfs(pRoot1, pRoot2) or dfs(pRoot1.left, pRoot2) or dfs(pRoot1.right, pRoot2)
def dfs(r1, r2):
    if not r2: return True
    if not r1: return False
    return r1.val == r2.val and dfs(r1.left, r2.left) and dfs(r1.right, r2.right)

