# Python Binary Trees

tags: data structures, python, trees

Binary trees are a tree data structure where each node has at most two children:
    - left node
    - right node

The leaves are the nodes at the very bottom of the tree
The depth is equal to the height of the tree

There are multiple types of binary trees:
    - Complete binary tree
      - complete at every level except possibly the last
    - Full binary tree
      - sometimes called a proper or plane binary tree
      - every node has either zero or two children

## Traversing Binary Trees

Traversal is the process of visiting or updating each node in a tree exactly once.
Trees may be traversed in multiple ways:
    - Depth-first
      - in-order
      - pre-order
      - post-order
    - Breadth-first

**Pre-Order Traversal**
 - start at root
 - check if root is empty
 - traverse left subtree by recursively calling pre-order
 - traverse right subtree by recursively calling preorder

**In-order Traversal**
 - start left
 - traverse left subtree by recursively calling in-order
 - display root or current node
 - traverse right subtree by recursively calling in-order

## Code
```python
#!/usr/bin/python3

# each node in the tree can have at most 2 children
# left child, right child
# leaf nodes are nodes without children
# a 'proper' or 'strict' binary tree is a binary tree that has 0 or 2 children
# a 'complete' binary tree is a tree where all levels except last are completely filled
#      and all nodes are as left as possible
# 'depth' is how deep in the tree a node is, starting at 0
# max depth is equal to the height of the tree

class Node(object):
    # define constructor
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)
    

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")
        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

    def preorder_print(self, start, traversal):
        """Root->Left->Right"""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        """Left->Root->Right"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal
    def postorder_print(self, start, traversal):
        """Left->Right->Root"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal = self.inorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal
 

# preorder:  1-2-3-4-5-6-7-8-
# inorder:   4-2-5-1-6-3-7-8- 
# postorder: 4-2-5-6-3-7-8-1- 
#        1
#      /   \
#     2     3
#    / \   / \
#   4   5 6   7
#              \
#               8


# set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)


print(tree.print_tree("preorder"))
print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))
```

Source: LucidProgramming : Binary Trees in Python: Introduction and Traversal Algorithms | youtube: https://www.youtube.com/watch?v=6oL-0TdVy28
