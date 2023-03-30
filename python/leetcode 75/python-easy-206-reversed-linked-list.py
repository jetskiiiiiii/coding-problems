"""
https://leetcode.com/problems/reverse-linked-list

pseudocode:
- if head empty, return head
- if head not empty, create new list with first value as node with val = head and next = None
- set head as the next node in linked list
- iterate through the linked list
- insert each node at the beginning of the new list, and set next = current node[0]
- set head as next node in linked list
- repeat same process until head = None, then return first item of new list
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is not None:
        nodes = [ListNode(head.val, None)]
        head = head.next
        while head:
            nodes.insert(0, ListNode(head.val, nodes[0]))
            head = head.next
        return nodes[0]
    else:
        return head


print(reverseList(head))
