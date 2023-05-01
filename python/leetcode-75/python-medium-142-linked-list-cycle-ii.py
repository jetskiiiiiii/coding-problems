"""
https://leetcode.com/problems/linked-list-cycle-ii/?envType=study-plan&id=level-1

pseudocode:

detectCycle:
- traverse linked list while keeping track of pointers in a seperate list
- for every iteration, check if curr.next is inside of list of pointers
- output start node of cycle

fastDetectCycle:
- traverse linked list
- if element already exists in set, return that element (start of the cycle)
- if not, add it to the set
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


def fastDetectCycle(head: Optional[ListNode]) -> Optional[ListNode]:
    references = set()
    while head:
        if head in references:
            return head
        references.add(head)
        head = head.next
    return None


print(fastDetectCycle(list))
