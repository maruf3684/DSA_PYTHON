class Node:
    data = None
    left = None
    right = None

    def __init__(self,data,left,right):
        self.data = data
        self.left = left
        self.right = right



class Tree:
    root = None

    def insert_tree(self,data):
        if self.root is None:
            first_node = Node(data,None,None)
            self.root = first_node
        else:
            iterator = self.root
            self.second_insertion(data, iterator)

    def second_insertion(self, data, iterator):
        if data < iterator.data:
            if iterator.left is not None:
                self.second_insertion(data, iterator.left)
            else:
                node = Node(data, None, None)
                iterator.left = node
        elif data > iterator.data:
            if iterator.right is not None:
                self.second_insertion(data, iterator.right)
            else:
                node = Node(data, None, None)
                iterator.right = node


    def delete_data(self,data,iterator,parent,iterator_is_left_child):
        if iterator is None:
            return
        if data == iterator.data:
            new_pointer = None
            if iterator.left is None and iterator.right is None:
                new_pointer = None
            elif iterator.left is None:
                new_pointer = iterator.right
            elif iterator.right is None:
                new_pointer = iterator.left
            else:
                # iterator has both child cases
                # Replace with the smallest node from the right subtree
                sub_iterator_parent = iterator
                sub_iterator = iterator.right
                while sub_iterator.left:
                    sub_iterator_parent = sub_iterator
                    sub_iterator = sub_iterator.left

                # replace the value
                iterator.data = sub_iterator.data

                # connect the right part if any
                # FIX: Check if successor is immediate right child or not
                if sub_iterator_parent == iterator:
                    # Successor is the immediate right child (no left movement)
                    sub_iterator_parent.right = sub_iterator.right
                else:
                    # Successor is deeper in a left chain
                    sub_iterator_parent.left = sub_iterator.right
                return
            if iterator_is_left_child:
                parent.left = new_pointer
            else:
                parent.right = new_pointer

        elif data < iterator.data:
            self.delete_data(data, iterator.left,iterator,True)
        elif data > iterator.data:
            self.delete_data(data, iterator.right,iterator,False)



    def pre_traverse(self,root):
        if root is None:
            return
        print(root.data, end=" ")
        self.pre_traverse(root.left)
        self.pre_traverse(root.right)


    def in_traverse(self, root):
        if root is None:
            return
        self.in_traverse(root.left)  # Left first
        print(root.data, end=" ")  # Then root
        self.in_traverse(root.right)  # Then right


tree = Tree()
tree.insert_tree(3)
tree.insert_tree(2)
tree.insert_tree(5)
tree.insert_tree(1)
tree.insert_tree(4)
tree.insert_tree(6)
tree.insert_tree(7)

tree.pre_traverse(tree.root)
print("\n---------------------")
tree.in_traverse(tree.root)

tree.delete_data(5,tree.root,None,True)

print("\n.........After Delete.........")

tree.pre_traverse(tree.root)
print("\n---------------------")
tree.in_traverse(tree.root)









"""
        3
      /   \
     2     5
    /     / \
   1     4   6
              \
               7

"""

"""
  delete rules if both child present:
  1. Replace with largest node from left subtree
     or 
  2. Replace with smallest node from right subtree
"""
