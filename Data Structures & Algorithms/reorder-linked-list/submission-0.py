# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_head = slow.next
        slow.next = None

        prev = None
        curr = second_head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        head1 = head
        head2 = prev

        while head2:
            tmp1 = head1.next
            tmp2 = head2.next

            head1.next = head2
            head2.next = tmp1
            head2 = tmp2
            head1 = tmp1

        curr = head
        while curr:
            print(curr.val)
            curr = curr.next

