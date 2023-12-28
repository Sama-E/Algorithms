# Write a function that takes in a Binary Search Tree (BST) and a target
# integer value and returns the closest value to that target value 
# contained in the BST.

# You can assume that there will only be one closest value.

# Each BST node has an integer value, a left child node, and a right
# child node. A node is said to be a calid BST node if and only if
# and only if it satisfies the BST property: its value is strictly
# greater than the values of every node to its left; its value is 
# less than or equal to the values of every node to its right; and 
# its children nodes are either valid BST nodes themselves or None / null.


def findClosestValueInBst(tree, target):
    node = tree
    closest = float("inf")

    while node is not None:
        closest = node.value if abs(node.value - target) < abs(closest - target) else closest

        if node.value < target:
            node = node.right
            continue
        node = node.left
    
    return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None