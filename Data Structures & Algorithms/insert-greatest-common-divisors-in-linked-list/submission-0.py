# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr:
            if curr.next:
                gcd = math.gcd(curr.val, curr.next.val)
                tmp = ListNode(gcd)
                nextNode = curr.next
                curr.next = tmp
                tmp.next = nextNode
                curr = nextNode
            else:
                curr = curr.next
        return head