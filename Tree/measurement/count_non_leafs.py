from Tree.base.binary_tree import build_sample_tree



def count_non_leafs(root):
    if root is None:
        return 0
    if root.left is not None and root.right is not None:
        left_count = count_non_leafs(root.left)
        right_count = count_non_leafs(root.right)
        current = 1
        return left_count + right_count + current
    else:
        left_count = count_non_leafs(root.left)
        right_count = count_non_leafs(root.right)
        return left_count + right_count


ans = count_non_leafs(build_sample_tree())
print(ans)



def count_non_leafs(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 0

    left_count = count_non_leafs(root.left)
    right_count = count_non_leafs(root.right)
    return left_count + right_count + 1


ans = count_non_leafs(build_sample_tree())
print(ans)