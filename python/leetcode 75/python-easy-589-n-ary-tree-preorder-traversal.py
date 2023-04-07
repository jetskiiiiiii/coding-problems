"""
https://leetcode.com/problems/n-ary-tree-preorder-traversal

preorder:
- use recursion
- if root is not None, append its value to results list
- if root is None, children attribute doesn't exists for NoneType, so recursion for children only happens inside of root if statement
- if the root is not None, and it has children, then for every child, set the child as root and perform the preorder() function on it
"""

from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


results = []


def preorder(root: "Node") -> List[int]:
    if root:
        results.append(root.val)
        if root.children:
            for i in root.children:
                preorder(i)
        return results


def fastPreorder(root: "Node") -> List[int]:
    results = []
    stack = []
    while root:
        root.append(root.val)
        if root.children:
            root = root.children
            # HOW TO CLIMB UP
    pass


# print(fastPreorder(node))
