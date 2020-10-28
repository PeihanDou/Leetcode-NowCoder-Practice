'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则返回true,否则返回false。假设输入的数组的任意两个数字都互不相同。
'''
# 后序数列的最后一个数必是根节点，以此为分界，若能把seq[:-1]分为两个子树，则递归判断子树，否则返回False
# 对两个子树重复上述操作
# O(nlogn)
def VerifySquenceOfBST(sequence):
        # write code here
        if not sequence: return False
        return isBST(sequence, 0, len(sequence)-1)
        
def isBST(seq, start, end):
    if start >= end: return True
    pivot = start
    while pivot < end and seq[pivot] < seq[end]:
        pivot += 1
    if min(seq[pivot:end+1]) < seq[end]: return False
    return isBST(seq, start, pivot-1) and isBST(seq, pivot, end-1)

# 单调栈 O(n)
# 前提： BST有左<根<右，后序遍历为左右根，那么如果从右往左遍历这个序列
# 遇见更大的，则为右子树， 入栈
# 若遇见小的， 说明是左子树（可能是当前节点的左子树，也可能是父辈节点的左子树），这是因为左子树必有max的约束
# 循环弹栈（就是说，在右子树上不断向根走去，知道到达这个左子树为之根的那个节点），设为max约束
# 如果大于mmax则False，不能形成二叉树
def VerifySquenceOfBST1(self, sequence):
    # write code here
    if not sequence: return False
    stack = [float('-inf')]
    mmax = float('inf')
    for s in sequence[::-1]:
        if s > mmax: return False
        
        while s < stack[-1]:
            mmax = stack.pop()
        stack.append(s)
    return True
