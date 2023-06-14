"""
Binary Tree implementation

This aims to replicate the creation and traversal of a binary tree from scratch
"""

class Node:
    def __init__(self,value) -> None:
        self.left = None
        self.right = None
        self.value = value

class BinaryTree:
    """
    Creation of binary tree class requiring initial value to be passed in as a root value

    Methods:
    print_tree(traversal_type) - prints the tree in the specified traversal type
    preorder_print(start,traversal) - prints the tree in preorder traversal
    inorder_print(start,traversal) - prints the tree in inorder traversal
    postorder_print(start,traversal) - prints the tree in postorder traversal
    height(node) - returns the height of the tree
    size_recursive(node) - returns the size of the tree using recursion
    find(node,data) - returns True if the data is found in the tree
    """
    def __init__(self,root) -> None:
        self.root = Node(root)

    def print_tree(self,traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root,"")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root,"")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root,"")
        else:
            print("Traversal type " + str(traversal_type) + " is not supported")
            return False

    def preorder_print(self,start,traversal):
        """Root->Left->Right"""
        if start:
            traversal += (str(start.value) + "->")
            traversal = self.preorder_print(start.left,traversal)
            traversal = self.preorder_print(start.right,traversal)
        return traversal

    def inorder_print(self,start,traversal):
        """Left->Root->Right"""
        if start:
            traversal = self.inorder_print(start.left,traversal)
            traversal += (str(start.value) + "->")
            traversal = self.inorder_print(start.right,traversal)
        return traversal

    def postorder_print(self,start,traversal):
        """Left->Right->Root"""
        if start:
            traversal = self.postorder_print(start.left,traversal)
            traversal = self.postorder_print(start.right,traversal)
            traversal += (str(start.value) + "->")
        return traversal
    
    def height(self,node):
        if node is None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return 1 + max(left_height,right_height)
       
    def size_recursive(self,node):
        if node is None:
            return 0
        return 1 + self.size_recursive(node.left) + self.size_recursive(node.right)

    def find(self,node,data):
        if not node:
            return False
        if node.value == data:
            return True
        return self.find(node.left,data) or self.find(node.right,data)
        



# Create a tree
tree = BinaryTree(1)
tree.root.left = Node(12)
tree.root.right = Node(9)
tree.root.left.left = Node(5)
tree.root.left.right = Node(6)

# Print the tree
print(f"Inorder traversal:") 
print(f"{tree.print_tree('inorder')}\n")

print(f"Preorder traversal:")
print(f"{tree.print_tree('preorder')}\n")

print(f"Postorder traversal:")
print(f"{tree.print_tree('postorder')}\n")

# find size of tree
print(f"Size of tree: {tree.size_recursive(tree.root)}\n")

# find element
print(f"Does element value 12 exist: {tree.find(tree.root,12)}\n")

# find height of tree
print(f"Height of tree: {tree.height(tree.root)}\n")