'''
###########好题###########
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。
'''
# 用prev存放当前节点的前一个节点
# 中序遍历，那么prev和当前节点就会相邻，那么prev.right = node, node.left = prev即可
class Solution:
    def __init__(self):
        self.prev = None
#         self.root = None
    def Convert(self, pRootOfTree):
        # write code here
        # 终止条件
        if pRootOfTree == None:
            return
        # 中序遍历，左子树
        # 左右孩子都有的节点不用调整指针 
        self.Convert(pRootOfTree.left)
        # 第一次是最左边的叶节点，下一次是对应的兄弟节点（如果有的话）
        if self.prev != None:
            pRootOfTree.left = self.prev
            self.prev.right = pRootOfTree
        self.prev = pRootOfTree
        self.Convert(pRootOfTree.right)
        return self.prev