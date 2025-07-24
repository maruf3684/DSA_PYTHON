from Tree.base.binary_tree import build_sample_tree



def count_leavs(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1

    left_count = count_leavs(root.left)
    right_count = count_leavs(root.right)

    return left_count + right_count


ans = count_leavs(build_sample_tree())
print(ans)