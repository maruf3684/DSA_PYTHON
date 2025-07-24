class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def build_sample_tree_two():
    nodes = [TreeNode(i) for i in range(16)]  # index 0 unused
    for i in range(1, 8):  # parent nodes: 1 to 7
        nodes[i].left = nodes[2 * i]
        nodes[i].right = nodes[2 * i + 1]
    return nodes[1]  # root

if __name__ == '__main__':
    tree = build_sample_tree_two()
    print(tree.val)  # prints 1