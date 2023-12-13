# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.head = None
        self.val = val
        self.next = next

    def append(self, val):
        if not self.head:
            self.head = ListNode(val, None)
            return

        node = self.head
        while node.next:
            node = node.next
        node.next = ListNode(val, None)


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_l = ListNode()
        while (list1 != None or list2 != None):
            if list1.val >= list2.val:
                new_l.append(list1.val)
                list1 = list1.next
            else:
                new_l.append(list2.val)
                list2 = list2.next
        while (list1.next != None):
            new_l.append(list1.val)

        while (list2.next != None):
            new_l.append(list1.val)

        return new_l




