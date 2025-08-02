from Tree.base.balance_and_non_balance_binary_tree import build_balanced_tree,build_unbalanced_tree

balance = build_balanced_tree()
unbalanced = build_unbalanced_tree()

balancer = True
def check_balanced(head):
    global balancer
    if balancer:
        if head is None:
            return 0
        current = 1
        left = check_balanced(head.left)
        right = check_balanced(head.right)

        if abs(left - right) > 1:
            balancer = False

        return current + max(left, right)
    else:
        return 0



# print(check_balanced(unbalanced))
# print(balancer)

print(check_balanced(balance))
print(balancer)




