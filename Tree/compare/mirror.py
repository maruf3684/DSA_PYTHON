from Tree.base.binary_tree import build_sample_tree, mirror_tree
from Tree.base.binary_tree_two import build_sample_tree_two

tree1 = build_sample_tree()
tree2 = mirror_tree(tree1)
#tree2 = build_sample_tree()

def check_mirror(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True
    if tree1 is None or tree2 is None:
        return False
    if tree1.val != tree2.val:
        return False
    left = check_mirror(tree1.left, tree2.right)
    if left:
        right = check_mirror(tree1.right, tree2.left)
    else:
        return False
    return left and right

print(check_mirror(tree1, tree2))