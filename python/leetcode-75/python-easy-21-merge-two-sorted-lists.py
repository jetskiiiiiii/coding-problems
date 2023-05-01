"""
https://leetcode.com/problems/merge-two-sorted-lists/?envType=study-plan&id=level-1

pseudocode:

mergeTwoLists:
- use a list to store merged nodes
- set the first node to a default node
- iterate through both lists until end
- for one list to iterate, the current value of that list must be smaller than the current value of the other list
- the current value that meets that requirement gets inserted in the list
- before appending the new node, the previous node's next value should be redirected to point to the new node, so that all items in the list connect
- at the end, one of the lists will be left with 1 value
- find the list with one value and append it to the list
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))  # [1,1,2,3,4,4]

# list1, list2 = ListNode(), ListNode()  # []

# list1, list2 = ListNode(), ListNode(0)  # [0]


def mergeTwoLists(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    nodes = [ListNode()]

    while list1 and list2:
        if list2.val < list1.val:
            nodes[-1].next = list2
            nodes.append(list2)
            list2 = list2.next
        else:
            nodes[-1].next = list1
            nodes.append(list1)
            list1 = list1.next

    if list1 == None:
        nodes[-1].next = list2
        nodes.append(list2)
    else:
        nodes[-1].next = list1
        nodes.append(list1)

    return nodes[1]
    # return [i.val for i in nodes[1:]]


print(mergeTwoLists(list1, list2))
