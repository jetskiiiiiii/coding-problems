"""
BFS:
- first in, first out (FIFO)
- root node initially inside of queue
- pop queue to get current element
- for every element add any existing children to queue
"""
from typing import List


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


node_3 = Node(3, Node(9), Node(20, Node(15), Node(7)))


def breadthFirstSearch(root: "Node") -> List[int]:
    queue = [root]
    results = []
    while queue:
        root = queue.pop()
        results.append(root.val)
        if root.left:
            queue.insert(0, root.left)
        if root.right:
            queue.insert(0, root.right)
    return results


print(breadthFirstSearch(node_3))
