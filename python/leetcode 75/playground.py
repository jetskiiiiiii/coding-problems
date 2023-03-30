class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


list = ListNode(1, ListNode(2, ListNode(0, ListNode(4, ListNode(2)))))
nodes = [list.val]
while list:
    try:
        if 
    nodes.append(list.next.val)
    list = list.next

print(nodes)
