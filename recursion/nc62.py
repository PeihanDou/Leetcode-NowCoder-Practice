'''
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
在这里，我们只需要考虑其平衡性，不需要考虑其是不是排序二叉树
平衡二叉树（Balanced Binary Tree），具有以下性质：
它是一棵空树或它的左右两个子树的高度差的绝对值不超过1，并且左右两个子树都是一棵平衡二叉树。
'''
# 由于递归是深度遍历，因此更深的的树不是平衡树的时候返回一个flag，上层的树遇到flag直接可以判断不平衡
# 自底而上
def IsBalanced_Solution(self, pRoot):
        # write code here
        if not pRoot: return True
        def depth(root):
            if not root: return 0
            left = depth(root.left)
            if left == -1: return -1
            right = depth(root.right)
            if right == -1: return -1
            if abs(left - right) > 1:
                return -1
            else:
                return 1 + max(left, right)
        return depth(pRoot) != -1