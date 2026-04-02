class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow = head
        fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = None
        
        reversed_node = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = reversed_node
            reversed_node = curr
            curr = next_node

        first, second = head, reversed_node
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            if not tmp1:
                break
            second.next = tmp1
            first = tmp1
            second = tmp2