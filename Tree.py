class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def generate_tree(l):
    if not l:
        return None