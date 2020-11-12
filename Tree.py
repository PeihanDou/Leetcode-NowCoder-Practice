class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def generate_Tree(l):
    root = TreeNode(l[0])
    l.pop(0)
    q = [root]
    while l:
        temp = []
        for node in q:
            if node:
                node.left = TreeNode(l.pop(0))
                temp.append(node.left)
                node.right = TreeNode(l.pop(0))
                temp.append(node.right)
        q = temp
    return root
# 递归 遍历
def preorder(root, res):
    if not root: return None
    res.append(root.val)
    preorder(root.left, res)
    preorder(root.right, res)
    return res

def inorder(root, res):
    if not root: return None
    preorder(root.left, res)
    res.append(root.val)
    preorder(root.right, res)
    return res

def postorder(root, res):
    if not root: return None
    preorder(root.left, res)
    preorder(root.right, res)
    res.append(root.val)
    return res

def inorder_flat(root):
    if not root:
        return []
    res = []
    stack = []
    node = root
    
    while node or stack:
        while node: # 找到最左边的节点
            stack.append(node)
            node = node.left
        node = stack.pop() # 弹出父节点
        res.append(node.val)
        node = node.right
    return res

def preorder_flat(root):
    if not root:
        return []
    res = []
    stack = []
    node = root
    
    while node or stack:
        while node: # 找到最左边的节点
            res.append(node.val)
            stack.append(node)
            node = node.left
        node = stack.pop() # 弹出父节点
        node = node.right
    return res

def postorder_flat(root):
    s=[]
    s.append(root)
    res = []
    lastNode=None #上一个访问过(打印出来)的节点
    while s:
        while s[-1].left: # 使用while到达其分支最底层的左节点
            s.append(s[-1].left)
        while s:
            # 如果当前节点的右节点为空或者已经访问过时，此时当前节点已经遍历完成，出栈，并打印
            if s[-1].right==lastNode or not s[-1].right:
                node=s.pop()
                res.append(node.val)
                lastNode=node
            elif s[-1].right: #如果当前节点的右节点没有访问过，则当前节点入栈
                s.append(s[-1].right)
                break #对新入栈的节点，重复走到最左边节点的过程
    return res

a = [1,2,3,4,5,6,7]
root = generate_Tree(a)
print(postorder_flat(root))
