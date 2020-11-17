'''
找一个二叉树中的最大路径和，路径的起点和终点可以是任意节点
'''

class Solution:
    def maxPathSum(self , root ):
        # write code here
        if not root: return 0
        self.maxpath = float('-inf')

        def findsum(root):
            # 找到以该节点为起点的最大路径
            if not root: return 0
            left = max(0,findsum(root.left))
            right = max(0,findsum(root.right))
            # left和right分别为左右孩子为起点的最大路径
            # 那么最大路径应该为：
            self.maxpath = max(self.maxpath, left+right+root.val)
            # 注意返回的应该是以root为起点的最大路径，因此只能是root+left或者root+right
            return max(left, right) + root.val
        # 由于findsum会遍历所有节点，所以maxpath记录的是 对每个节点来说，过这个节点的最大路径 的最大值
        # 因此不用考虑root.val小于0的情况，因为即使这样， left和right的值也会记录在maxpath里
        findsum(root)
        return self.maxpath