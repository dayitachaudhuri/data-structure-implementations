# ---------------------------------------
# Binary Tree Node
#----------------------------------------

class TreeNode:
    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None
    
# ---------------------------------------
# Binary Search Tree
#----------------------------------------

class BST:
    def __init__(self):
        self.root = None
        self.count = 0
    
    # Add a node
    def addNode(self, newVal):
        self.root = addHelper(self.root, newVal)
        self.count += 1

    # delete a Node
    def deleteNode(self, currVal):
        if not self.root:
            print("Empty Tree")
        else:
            self.root = deleteHelper(self.root, currVal)
            self.count -= 1
    
    # Print the Tree
    def display(self):
        indent = self.count
        q = [self.root]
        while q:
            temp = []
            print(" " * indent, end = "")
            for item in q:
                print(item.val, end=" ")
                if item.left:
                    temp.append(item.left)
                if item.right:
                    temp.append(item.right)
            print()
            q = temp
            indent -= 1

#----------------------------------------
# Helper Functions

def addHelper(node, newVal):
    if not node:
        return TreeNode(newVal)
    if node.val < newVal:
        node.right = addHelper(node.right, newVal)
    elif node.val > newVal:
        node.left = addHelper(node.left, newVal)
    return node    

def deleteHelper(node, currVal):
    if not node:
        return node
    if currVal < node.val:
        node.left = deleteHelper(node.left, currVal)
    elif currVal > node.val:
        node.right = deleteHelper(node.right, currVal)
    else:
        if not node.left:
            return node.right
        elif not node.right:
            return node.left
        else:
            if not node.left.right:
                node.val = node.left.val
                node.left = node.left.left
            else:
                itr = node.left
                while itr.right and itr.right.right:
                    itr = itr.right
                node.val = itr.right.val
                itr.right = itr.right.left
    return node

# ---------------------------------------
# Balanced Binary Search Tree (AVL TREE)
#----------------------------------------

class BalancedBST:
    def __init__(self):
        self.root = None
        self.count = 0
    
    # Add a node
    def addNode(self, newVal):
        self.root = addHelperBalanced(self.root, newVal)
        self.count += 1

    # delete a Node
    def deleteNode(self, currVal):
        if not self.root:
            print("Empty Tree")
        else:
            self.root = deleteHelperBalanced(self.root, currVal)
            self.count -= 1
    
    # Print the Tree
    def display(self):
        indent = self.count
        q = [self.root]
        while q:
            temp = []
            print(" " * indent, end = "")
            for item in q:
                print(item.val, end=" ")
                if item.left:
                    temp.append(item.left)
                if item.right:
                    temp.append(item.right)
            print()
            q = temp
            indent -= 1

# ---------------------------------------
# Rotations

def LLRotation(node):
    newNode = node.left
    node.left = newNode.right
    newNode.right = node
    return newNode

def RRRotation(node):
    newNode = node.right
    node.right = newNode.left
    newNode.left = node
    return newNode

def LRRotation(node):
    node.left = RRRotation(node.left)
    return LLRotation(node)

def RLRotation(node):
    node.right = LLRotation(node.right)
    return LLRotation(node)

# ---------------------------------------
# Helper Functions

def height(node):
    if not node:
        return 0
    return 1 + max(height(node.left), height(node.right))

def addHelperBalanced(node, newVal):
    if not node:
        return TreeNode(newVal)
    if node.val < newVal:
        node.right = addHelperBalanced(node.right, newVal)
        if abs(height(node.right) - height(node.left)) > 1:
            if node.right.val < newVal:
                node = RRRotation(node)
            else:
                node = RLRotation(node)
    elif node.val > newVal:
        node.left = addHelperBalanced(node.left, newVal)
        if abs(height(node.right) - height(node.left)) > 1:
            if node.left.val > newVal:
                node = LLRotation(node)
            else:
                node = LRRotation(node)
    return node    

def deleteHelperBalanced(node, currVal):
    if not node:
        return node
    if currVal < node.val:
        node.left = deleteHelperBalanced(node.left, currVal)
        if abs(height(node.right) - height(node.left)) > 1:
            if node.left.val < currVal:
                node = LLRotation(node)
            else:
                node = LRRotation(node)
    elif currVal > node.val:
        node.right = deleteHelperBalanced(node.right, currVal)
        if abs(height(node.right) - height(node.left)) > 1:
            if node.right.val > currVal:
                node = RRRotation(node)
            else:
                node = RLRotation(node)
    else:
        if not node.left:
            return node.right
        elif not node.right:
            return node.left
        else:
            if not node.left.right:
                node.val = node.left.val
                node.left = node.left.left
            else:
                itr = node.left
                while itr.right and itr.right.right:
                    itr = itr.right
                node.val = itr.right.val
                itr.right = itr.right.left
    return node

# ---------------------------------------
# Driver Function
#----------------------------------------
def main():
    # BST
    tree = BST()
    tree.addNode(10)
    tree.addNode(8)
    tree.addNode(7)
    tree.addNode(6)
    tree.addNode(5)
    tree.addNode(4)
    tree.display()

    # AVL Tree
    tree2 = BalancedBST()
    tree2.addNode(10)
    tree2.addNode(8)
    tree2.addNode(7)
    tree2.addNode(6)
    tree2.addNode(5)
    tree2.addNode(4)
    tree2.display()


if __name__ == '__main__':
    main()