from collections import deque
from Tree.base.binary_tree import build_sample_tree

tree = build_sample_tree()


#                1 [-> 2,3 ]  -r
#         - r  2,3  [ 4,5,6,7<-]
#            7,6,5,4  [8,9,10,11,12,13,14,15 ]  -r
#      -r 8,9,10,11,12,13,14,15  [ ]
#
# Rules:
#  # right there q read korle -right node age push hobe - but q er left die push hobe.
#  # left there q read korle -left node age push hoe - but q er right die push hobe.
#


def level_order_spiral_efficient(root,read_from_right):
    queue = deque()
    queue.append(root)
    window = queue.__len__()
    answer = []
    while queue:
        for _ in range(window):
            if read_from_right:
                node = queue.pop()
                answer.append(node.val)
                if node.right:
                    queue.appendleft(node.right)
                if node.left:
                    queue.appendleft(node.left)
            else:
                node = queue.popleft()
                answer.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        window = queue.__len__()
        read_from_right = not read_from_right

    print(answer)

level_order_spiral_efficient(tree, True)




