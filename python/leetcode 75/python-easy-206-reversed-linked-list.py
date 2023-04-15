"""
https://leetcode.com/problems/reverse-linked-list/?envType=study-plan&id=level-1

pseudocode:

reverseList
- if head empty, return head
- if head not empty, create new list with first value as node with val = head and next = None
- set head as the next node in linked list
- iterate through the linked list
- insert each node at the beginning of the new list, and set next = current node[0]
- set head as next node in linked list
- repeat same process until head = None, then return first item of new list

fast/fasterReverseList:
- create new nodes whose value is head (as we iterate through linked list) and whose next is previous nodes
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


def fastReverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    new_head = None
    # stop when head reaches end node (None)
    while head:
        # create new node where val is current value of head, and next is the previous made node
        new_head = ListNode(head.val, new_head)
        # iterate through head
        head = head.next
    return new_head


def fasterReverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    new_head = None
    # stop when head reaches end (None)
    while head:
        # hold the next node in list temporariliy
        temp = head.next
        # the next attribute of current node is what the reversed list currently is (with new_head representing the reversed list)
        head.next = new_head
        # update the reversed list to be the same as current node
        new_head = head
        # iterate through the list (as temp == head.next)
        head = temp

    return new_head


print(reverseList(head))
