# ---------------------------------------
# Balanced Binary Search Tree
#----------------------------------------

class TreeNode:
    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None
    
class BST:
    def __init__(self):
        self.root = None
    
    def addNode(self, val):
        self.root = addHelper(self.root, val)

    def deleteNode()

def addHelper(node, newVal):
    if not node:
        return TreeNode(newVal)
    if node.val < newVal:
        node.right = addHelper(node.right, newVal)
    elif node.val > newVal:
        node.left = addHelper(node.left, newVal)
    return node    