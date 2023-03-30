"""
https://leetcode.com/problems/linked-list-cycle-ii

pseudocode:

detectCycle:
- traverse linked list while keeping track of pointers in a seperate list
- for every iteration, check if curr.next is inside of list of pointers
- output start node of cycle

fastDetectCle:
- 
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


def detectCycle(head: Optional[ListNode]) -> Optional[ListNode]:
    # keep track of nodes in a separate list, with head already appended
    nodes = []
    # start iteration at head.next
    curr = head
    while curr:
        # if curr node is an index of the nodes list, return node where cycle starts
        if curr.next in nodes:
            return curr.next
        # if not an index in node list, python will throw error, in which case append node to list
        nodes.append(curr)
        # iterate to next node
        curr = curr.next
        # if linked list has no cycle, it will reach None and loop will end, so return null
    return None


def fastdetectCycle(head: Optional[ListNode]) -> Optional[ListNode]:
    pass


print(detectCycle(list))
