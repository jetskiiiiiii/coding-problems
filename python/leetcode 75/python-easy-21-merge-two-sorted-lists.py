"""
https://leetcode.com/problems/merge-two-sorted-lists/?envType=study-plan&id=level-1

pseudocode:

mergeTwoLists:
- create a list for merged results
- create 2 variables to get the next node for easier iteration
- create a temp variable to sort
- go through linked list until next == None
- compare 
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
    merged_list = ListNode()
    next_node_1, next_node_2, next_node_merge = list1.next, list2.next, merged_list.next
    hold_val = 0

    # determine head of merged list

    if list1.val > list2.val:
        merged_list.val = list2.val
        hold_val = list1.val
    else:
        merged_list.val = list1.val
        hold_val = list2.val

    while next_node_1 or next_node_2:
        if hold_val > next_node_1.val:
            next_node_merge.val = list1.next
            next_node_merge = next_node_merge.next
        else:
            next_node_merge.val = hold_val
            hold_val = next_node_1

    return merged_list.val


print(mergeTwoLists(list1, list2))
