from queue import Queue
from stack import Stack

"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # compare the input value with the value of the Node
        # if value < Node's value
        if value < self.value:
            # we need to go left
            # if we see that there is no left child,
            if self.left is None:
                # then we can wrap the value in a BSTNode and park it
                self.left = BSTNode(value)
            # otherwise there is a child
            else:
                # call the left child's `insert` method
                self.left.insert(value)
        # otherwise, value >= Node's value
        else:
            # we need to go right
            # if we see there is no right child,
            if self.right is None:
                # then we can wrap the value in a BSTNode and park it
                self.right = BSTNode(value)
            # otherwise there is a child
            else:
                # call the right child's `insert` method
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target: # if the value equals the target
            return True # return true

        if target < self.value: # if the target is less than the current value
            if not self.left: # if there's no left option
                return False # return false
            else: # if there is options left
                return self.left.contains(target) # return the left side and recheck
        else: # if the target is more than the current value
            if not self.right: # if there is no right value
                return False # return false
            else: # if there is right values
                return self.right.contains(target) # check the next value and recheck

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right: # if there is no value on the right ( a greater value )
            return self.value # return the current value
        else: # if there is values on the right
            return self.right.get_max() # run the get_max function again

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value) # calls the function on the node

        if self.left: # if there's values left
            self.left.for_each(fn) # call the function on each node

        if self.right: # if there's values right
            self.right.for_each(fn) # call the function on each node

#     # Part 2 -----------------------

# A search is completed when the target of the search is found. A traversal is completed when every node has been explored.

# A Depth First Traversal (DFT) is one that continues traveling forward on each branch until a dead end is reached. The search then retreats to the first unexplored branch and follows the next unexplored path until that one too reaches a dead end. This continues until all nodes have been visited. Think of it like being in a maze and always turning right at each intersection. We can do a DFT recursively or iteratively. The iterative approach makes use of stack.

# A Breadth First Traversal (BFT) takes the opposite strategy. We explore layer by layer, slowly moving outward from the starting point. At each node, we add every node we discover to the list of nodes to explore, then explore them in the order in which we encounter them. For this, we use a queue. This means we’ll jump around a bit - the next node we visit might not be directly connected to the one we are on.

#     # Print all the values in order from low to high
#     # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.left:
            self.left.in_order_print()
        print(self.value)
        if self.right:
            self.right.in_order_print()

# create queue
# add root to queue
# while queue is not empty
    # node = head of queue
    # add children of node to queue
    # pop node off the queue

#     # Print the value of every node, starting with the given node,
#     # in an iterative breadth first traversal
    def bft_print(self, cb):
        q = []
        q.append(self)

        while len(q):
            current_node = q.pop(0)
            print(current_node.value)
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)
            cb(current_node.value)

# create stack
# add root to stack
# while stack is not empty
    # node = pop top of stack
    # add children of node to stack

#     # Print the value of every node, starting with the given node,
#     # in an iterative depth first traversal
    def dft_print(self, cb):
        s = []
        s.append(self)

        while len(s):
            current_node = s.pop()
            print(self.value)
            if current_node.left:
                s.append(current_node.left)
            if current_node.right:
                s.append(current_node.right)
            cb(current_node.value)

#     # Stretch Goals -------------------------
#     # Note: Research may be required

#     # Print Pre-order recursive DFT
#     def pre_order_dft(self):
#         pass

#     # Print Post-order recursive DFT
#     def post_order_dft(self):
#         pass

# """
# This code is necessary for testing the `print` methods
# """
# bst = BSTNode(1)

# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)

# bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()
