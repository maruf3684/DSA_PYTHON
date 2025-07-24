from Tree.base.binary_tree import build_sample_tree
from Tree.base.binary_tree_two import build_sample_tree_two

tree1 = build_sample_tree()
tree2 = build_sample_tree_two()



def check_identical(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True
    if tree1 is None and tree2 is not None:
        return False
    if tree2 is None and tree1 is not None:
        return False

    left = check_identical(tree1.left, tree2.left)
    right = check_identical(tree1.right, tree2.right)

    return left and right




print(check_identical(tree1, tree2))