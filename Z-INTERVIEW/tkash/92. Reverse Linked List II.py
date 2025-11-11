

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def make_linked_list(arr):
    head = None
    tail = None

    for val in arr:
        new_node = Node(val)
        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node

    return head


head = make_linked_list([1, 2, 3, 4, 5])

def prt(head):
    while head:
        print(head.val)
        head=head.next

def reverse(head,left,right):
    prev = None
    curr = head
    while curr is not None:
        #kono akta point e tar prev element amake jante hobe
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    prt(prev)


def reverse_point(head,left,right):
    count = 0

    fst = None
    lst = None

    prev = None
    curr = head

    khel_shuru = None
    while curr:
        count = count+1

        if count == left -1:
            fst = curr
            curr = curr.next
        elif count == right+1:
            lst = curr
            curr = curr.next
        elif(count>=left and count <= right):
            if count == left:
                khel_shuru = curr

            next = curr.next
            curr.next = prev

            prev = curr
            curr = next
        else:
            curr = curr.next

    if fst != None:
        fst.next = prev
    if lst != None:
        khel_shuru.next = lst

    if fst != None:
        return head
    else:
        return prev
















reverse_point(head,1,1)