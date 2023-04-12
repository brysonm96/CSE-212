#binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#binary tree class
class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    #traverse function
    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.val)
            self.inorder_traversal(node.right)
    
    #reverse traverse function
    def reverse_traverse(self, node):
        if node:
            self.reverse_traverse(node.right)
            print(node.val)
            self.reverse_traverse(node.left)

#example node inputs
root = TreeNode(10)
root.left = TreeNode(7)
root.right = TreeNode(14)
root.left.left = TreeNode(3)
root.left.right = TreeNode(9)

tree = BinaryTree(root)
print("traversed data: ")
tree.inorder_traversal(root)
print("reversed data: ")
tree.reverse_traverse(root) 

#test cases
#traverse output: 2 3 4 5 7
#reverse output: 7 5 4 3 2
