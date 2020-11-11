'''给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
'''
class TreeNode():
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
        self.next = None # pointing to parent

# 写if else 从简单的情况开始写。也注意分类要尽可能包含所有情况
# 本题分类：
# 1. 有右孩子：下一个节点就是右孩子的最左边的左孩子
# 2. 没有右孩子，不是根节点：向上找父亲，检测如果父亲的左孩子的该节点，那下一个节点就是父节点。
# 否则继续找父亲，直到找到父节点左孩子是本节点的情况
# 3. 如果2遍历到了根节点还没有返回，说明一直是从右孩子找父亲，那么说明开始的节点是最后一个，直接返回None

def GetNext(self, pNode):
    # write code here
    if not pNode:
        return pNode
    if pNode.right: # 有右孩子
        pNode = pNode.right
        while pNode.left:
            pNode = pNode.left
        return pNode
    while pNode.next: # 没有右孩子，但不是根节点，则不断找父节点
        root = pNode.next
        if root.left == pNode: # 如果pNode是 root的左孩子，则下一个节点就是root，否则继续找父节点
            return root
        pNode = pNode.next
    return None