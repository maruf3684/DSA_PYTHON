from collections import deque
from Tree.base.binary_tree import build_sample_tree

tree = build_sample_tree()


def traverse(root):
    queue = deque()
    queue.append(root)
    size = queue.__len__()
    reversedx = False
    print(queue[0].val, end = " ")
    while queue:
        node = queue.popleft()
        size = size - 1

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

        if size == 0:
            size = queue.__len__()
            if reversedx:
                for item in reversed(queue):
                    print(item.val, end=" ")
            else:
                for item in queue:
                    print(item.val, end=" ")
            reversedx = not reversedx






traverse(tree)
