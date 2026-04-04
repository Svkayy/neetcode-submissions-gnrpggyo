# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        k = length - n + 1
        tmp = head
        if k == 1:
            return tmp.next
        
        count = 1
        while tmp:
            if count == k-1:
                tmp.next = tmp.next.next
                break
            tmp = tmp.next
            count += 1
        
        return head
            
