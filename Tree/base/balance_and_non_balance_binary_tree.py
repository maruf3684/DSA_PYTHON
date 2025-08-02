

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# -------------------------
# Balanced Binary Tree
# -------------------------
def build_balanced_tree():
    nodes = [TreeNode(i) for i in range(8)]  # nodes[0] unused
    nodes[1].left = nodes[2]
    nodes[1].right = nodes[3]
    nodes[2].left = nodes[4]
    nodes[2].right = nodes[5]
    nodes[3].left = nodes[6]
    nodes[3].right = nodes[7]
    return nodes[1]

# -------------------------
# Unbalanced Binary Tree
# -------------------------
def build_unbalanced_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)
    return root

# Optional: pre-order print to visualize
def print_preorder(node):
    if node:
        print(node.val, end=' ')
        print_preorder(node.left)
        print_preorder(node.right)

if __name__ == "__main__":
    print("Balanced Binary Tree (pre-order):")
    balanced = build_balanced_tree()
    print_preorder(balanced)
    print("\n")

    print("Unbalanced Binary Tree (pre-order):")
    unbalanced = build_unbalanced_tree()
    print_preorder(unbalanced)
    print()

    #
    #     1
    #    / \
    #   2   3
    #  /
    # 4

    #     1
    #    /
    #   2
    #  /
    # 3