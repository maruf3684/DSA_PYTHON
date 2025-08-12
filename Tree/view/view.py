from Tree.base.binary_tree import build_sample_tree
from collections import deque

given_tree = build_sample_tree()




def left_view(root):
    if root is None:
        return []
    q = deque()
    q.append(root)
    q_length = 1
    ans = []

    while q:
        for i in range(q_length):
            element = q.pop()
            if i == 0:
                ans.append(element.val)
            if element.right is not None:
                q.appendleft(element.right)
            if element.left is not None:
                q.appendleft(element.left)
        q_length = len(q)

    print(ans)
    return ans

left_view(given_tree)