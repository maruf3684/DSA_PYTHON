from Tree.base.binary_tree import build_sample_tree


def tree_sum(root):
    if root is None:
        return 0
    return root.val + tree_sum(root.left) + tree_sum(root.right)



sum = tree_sum(build_sample_tree())
print(sum)