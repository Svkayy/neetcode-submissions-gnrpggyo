# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1)
        curr1 = list1
        curr2 = list2
        tmp = head
        while curr1 and curr2:
            a = curr1.val
            b = curr2.val
            if a <= b:
                tmp.next = curr1
                tmp = tmp.next
                curr1 = curr1.next
            else:
                tmp.next = curr2
                tmp = tmp.next
                curr2 = curr2.next
        if curr1:
            tmp.next = curr1
        if curr2:
            tmp.next = curr2
        return head.next
        