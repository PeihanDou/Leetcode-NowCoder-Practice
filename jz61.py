class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
请实现两个函数，分别用来序列化和反序列化二叉树
'''

# 后序遍历法
def Serialize(root):
        # write code here
        stack = []
        def preorder(root):
            if root is None:
                stack.append('#')
                return None
            preorder(root.left)
            preorder(root.right)
            stack.append(str(root.val))
        preorder(root)
        return ' '.join(stack)
    
def Deserialize(s):
    # write code here
    l = s.split(" ")
    def des():
        val = l.pop(-1)
        if val == '#':
            return None
        node = TreeNode(int(val))
        node.right = des()
        node.left = des()
        return node
    node = des()
    return node