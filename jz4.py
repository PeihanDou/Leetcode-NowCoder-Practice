class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
输入某二叉树的前序遍历和中序遍历的结果，
请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
'''
'''
前序序列第一个数为根
在中序序列中找到这个数（假设角标为idx），则左边为左子树中序遍历，右边为右子树中序遍历，
前序序列的[1:1+idx]为左子树前序遍历，[1+idx:]为右子树前序遍历
'''

def reConstructBinaryTree(pre, tin):
        # write code here
        if len(pre) == 0:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        root = TreeNode(pre[0])
        idx = tin.index(pre[0])
        root.left = reConstructBinaryTree(pre[1:1+idx], tin[:idx])
        root.right = reConstructBinaryTree(pre[1+idx:], tin[idx+1:])
        return root

def rebuild(pre, tin):
    if len(pre) == 0:
        return None
    if len(pre) == 1:
        return TreeNode(pre[0])
    root = TreeNode(pre[0])
    index = tin.index(pre[0])
    root.left = rebuild(pre[1:1+index], tin[:index])
    root.right = rebuild(pre[1+index:], tin[index+1:])
    return root



# for test
pre = [1,2,4,7,3,5,6,8]
tin = [4,7,2,1,5,3,8,6]
def pretravel(root, res):
    if root:
        res.append(root.val)
        pretravel(root.left, res)
        pretravel(root.right, res)
    return res

tree = rebuild(pre, tin)

print(pretravel(tree, []))
