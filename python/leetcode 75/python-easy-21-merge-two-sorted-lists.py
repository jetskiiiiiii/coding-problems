"""
https://leetcode.com/problems/merge-two-sorted-lists/?envType=study-plan&id=level-1

pseudocode:

mergeTwoLists:
- for every element in list2, compare it with the elements in list1
- also keep track of previous node
- if list2 < list1, put list2 element right before the list1 element
- this new node should have a pointer to the list1 element which was found to be bigger than it
- the node behind it should have a pointer to the newly made node
- for the next iteration, start at the list1 element instead of the beginning
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


# def mergeTwoLists(
#     list1: Optional[ListNode], list2: Optional[ListNode]
# ) -> Optional[ListNode]:
#     new_nodes = [ListNode()]

#     while list1 != None and list2 != None:
#         if list2.val > list1.val:
#             new_nodes[-1].next = list1
#             new_nodes.append(ListNode(list1.val, None))
#             list1 = list1.next
#         elif list2.val <= list1.val:
#             new_nodes[-1].next = list2
#             new_nodes.append(ListNode(list2.val, None))
#             list2 = list2.next

#     # if list1 == None:
#     #     while list2 != None:
#     #         new_nodes[-1].next = list2
#     #         new_nodes.append(ListNode(list2.val, None))
#     #         list2 = list2.next
#     # elif list2 == None:
#     #     while list1 != None:
#     #         new_nodes[-1].next = list1
#     #         new_nodes.append(ListNode(list1.val, None))
#     #         list1 = list1.next

# return new_nodes[1]j
# # return [i.val for i in new_nodes]


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
