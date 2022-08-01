# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev


    #### RECURSIVE

def reverse_list_recursive(head, prev = None):
    if head is None:
        return prev

    next = head.next
    head.next = prev

    return reverse_list_recursive(next, head)