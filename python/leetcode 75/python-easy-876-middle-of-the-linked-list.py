"""
https://leetcode.com/problems/middle-of-the-linked-list

pseudocode:

middleNode:
- traverse linked list and keep track of how many iterations it takes to get to end of list
- traverse the reverse linked list again to half as many iterations as it took to get to end of list
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
list2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))


def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    curr = head
    count = 0
    while curr:
        curr = curr.next
        count += 1
    curr = head
    for _ in range(1, int(count / 2) + 1):
        curr = curr.next
    return curr


print(middleNode(list2))
