"""
Linear Search:
- brute force search
- starts at first item and goes through each item sequentially

O(n)
"""


# create linked list
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


root = Node(1, Node(2, Node(3)))


def linearSearch(root: "Node", target: int) -> bool:
    while root:
        if root.val == target:
            return True
        root = root.next
    return False


print(linearSearch(root, 4))
