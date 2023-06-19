"""
Binary Search Tree implementation

This aims to replicate the creation and traversal of a binary search tree from scratch
"""

class Node:
    def __init__(self,value) -> None:
        self.left = None
        self.right = None
        self.value = value

class BinarySearchTree:
    def __init__(self,root) -> None:
        self.root = root
    
    def insert(root,value):
        if root is None:
            return Node(value)
        elif root.value < value:
            root.right = insert(root.right,value)
        else:
            root.left = insert(root.left,value)
        return root
    
    def inorder_print(self,start,traversal):
        """Left->Root->Right"""
        if start:
            traversal = self.inorder_print(start.left,traversal)
            traversal += (str(start.value) + "->")
            traversal = self.inorder_print(start.right,traversal)
        return traversal
# Test
tree = BinarySearchTree(1)
tree.insert(tree.root,2)
tree.insert(tree.root,4)
tree.insert(tree.root,3)
print(tree.inorder_print(tree.root,""))
