from Tree.base.binary_tree import build_sample_tree


count = 0
def tree_size(root):
    global count
    if root is None:
        return
    #print(root.val)
    count+=1
    tree_size(root.left)
    tree_size(root.right)

tree_size(build_sample_tree())
print(count)




# def tree_size2(root):
#     if root is None:
#         return 0
#     return 1 + tree_size2(root.left) + tree_size2(root.right)
#
#
# count2 = tree_size2(build_sample_tree())
# print(count2)


def tree_size2(root):
    if root is None:
        return 0
    left = tree_size2(root.left)
    right = tree_size2(root.right)
    current = 1
    return left + right + current


count2 = tree_size2(build_sample_tree())
print(count2)