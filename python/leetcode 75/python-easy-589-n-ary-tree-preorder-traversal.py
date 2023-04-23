"""
https://leetcode.com/problems/n-ary-tree-preorder-traversal/?envType=study-plan&id=level-1

preorder:
- use recursion
- if root is not None, append its value to results list
- if root is None, children attribute doesn't exists for NoneType, so recursion for children only happens inside of root if statement
- if the root is not None, and it has children, then for every child, set the child as root and perform the preorder() function on it

fastPreorder:
- append root to results
- if    
"""

from typing import List

node = [1, [[3, [5, 6]], 2, 4]]
# node = [1, [2, [3, [6, [7, [11, [14]]]]], [4, [8, [12]]], [5, [[9, [13]], 10]]]]
node = [1, [3, 2, 4]]


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def recrusivePreorder(self, root, results=None):
    if results == None:
        results = []
    if root:
        results.append(root.val)
        if root.children:
            for i in root.children:
                preorder(i, results)
    return results


def fastPreorder(root: "Node") -> List[int]:
    results = []
    stack = set(root)
    i = 0
    while len(stack) != 0:
        # append root to results
        results.append(root.val)
        # check if root has no child or list of children (including None)
        if root.children == None:
            # ERROR: CAN'T REMOVE "LAST ELEMENT" (NOT TRUE STACK IMPLIMENTATION)
            stack.remove()
        else:
            stack.add(root)
            root = root.children[i]
            i += 1
    return results


# children are always lists; empty list means no children


def fastPreorder(root: "Node") -> List[int]:
    # ERROR: WHEN STACK POPS, PROGRAM FORGETS THE INDEX OF PREVIOUS LIST
    # WHEN GOING UP THE TREE, PROGRAM FORGETS WHICH CHILDREN IT LEFT OFF AT
    results, stack = [root.val], [root.children]
    while stack:
        for i in stack[-1]:
            results.append(i.val)
            if i.children != []:
                stack.append(i.children)
                break
            if i == stack[-1][-1]:
                stack.pop()
    return results


print(fastPreorder(node))
