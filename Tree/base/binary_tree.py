class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def build_sample_tree():
    nodes = [TreeNode(i) for i in range(17)]  # index 0 unused, up to 16
    for i in range(1, 8):  # 1 to 7 have both left and right children
        nodes[i].left = nodes[2 * i]
        nodes[i].right = nodes[2 * i + 1]
    # Add extra node 16 as left child of node 8
    nodes[8].left = nodes[16]
    return nodes[1]  # root

def mirror_tree(node):
    if node is None:
        return None
    new_node = TreeNode(node.val)
    new_node.left = mirror_tree(node.right)
    new_node.right = mirror_tree(node.left)
    return new_node

def print_preorder(node):
    if node:
        print(node.val, end=' ')
        print_preorder(node.left)
        print_preorder(node.right)

if __name__ == '__main__':
    original = build_sample_tree()
    mirror = mirror_tree(original)

    print("Original tree (pre-order):")
    print_preorder(original)

    print("\nMirrored tree (pre-order):")
    print_preorder(mirror)