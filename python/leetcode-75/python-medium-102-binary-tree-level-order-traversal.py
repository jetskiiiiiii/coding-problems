"""
https://leetcode.com/problems/binary-tree-level-order-traversal/

levelOrder:
** results must be type List[List[int]], meaning levels must be accounted for
- use queue to traverse level by level
- use None markers to indicate a new level
- if a None marker is reached, and queue is empty, all levels have been traversed
"""

from typing import List


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


node_15 = TreeNode(15)
node_7 = TreeNode(7)
node_20 = TreeNode(20, node_15, node_7)
node_9 = TreeNode(9)
node_3 = TreeNode(3, node_9, node_20)

node_1 = TreeNode(1)

node_empty = TreeNode()


def levelOrder(root: "TreeNode") -> List[List[int]]:
    # if root is None, return empty list
    if not root.val:
        return []

    # keep track of levels with None marker
    queue = [None, root]
    results = [[]]
    while queue:
        root = queue.pop()

        # if None is encountered, and queue is empty, all levels have been traversed
        if not root and not queue:
            return results

        # if None is encountered but queue is not empty, new level reached, add None to end of queue to indicate end of level
        elif not root:
            results.append([])  # add a new list to represent a new level
            queue.insert(0, None)
            continue  # if None is encountered, don't add to results

        # if a real value is encountered, append it to results
        results[-1].append(root.val)
        if root.left:
            queue.insert(0, root.left)
        if root.right:
            queue.insert(0, root.right)
    return results


print(levelOrder(node_empty))
