# main.py

from Tree.base.binary_tree import build_sample_tree

def inorder_traversal(root):
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

# Load the tree
root = build_sample_tree()
print("Inorder Traversal:", inorder_traversal(root))