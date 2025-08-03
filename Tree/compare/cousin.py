from Tree.base.binary_tree import build_sample_tree
from collections import deque

head = build_sample_tree()


def check_cousin(head,item1,item2):
    queue = deque()
    queue.append((None,head))
    size = len(queue)
    while queue:
        found1 = None
        found2 = None
        for _ in range(size):
            item = queue.popleft()
            node = item[1]
            parent = item[0]

            print(node.val)

            if found1 is None and node.val == item1:
                found1 = parent
                print(f"found1 = {found1}")
            if found2 is None and node.val == item2:
                found2 = parent
                print(f"found2 = {found2}")

            if found1 is not None and found2 is not None and found1 != found2:
                return True

            if node.left:
                queue.append((node.val,node.left))
            if node.right:
                queue.append((node.val,node.right))

        size = len(queue)
    return False




ans = check_cousin(head,4,5)
print()
print(ans)