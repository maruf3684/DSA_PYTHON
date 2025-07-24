from Tree.base.binary_tree import build_sample_tree

def calculate_height(root):
    if root is None:
        return 0
    left_height = calculate_height(root.left)
    right_height = calculate_height(root.right)
    return 1 + max(left_height, right_height)


h = calculate_height(build_sample_tree())
print(h)