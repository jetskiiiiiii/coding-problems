"""
https://leetcode.com/problems/binary-tree-level-order-traversal/

levelOrder:
- use queue to get queue[0] (every level resets the stack)
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


# ERROR: function does not group values by level
def levelOrder(root: "TreeNode") -> List[List[int]]:
    queue = [root.left, root.right]
    results = [root.val]
    while queue != []:
        results.append(queue[0].val)
        if queue[0].left != None:
            queue.append(queue[0].left)
        if queue[0].right != None:
            queue.append(queue[0].right)
        queue = queue[1:]
    return results


print(levelOrder(node_3))
