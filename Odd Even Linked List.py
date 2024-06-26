# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        begin = head
        prev = head
        if head:
            head = head.next
        else:
            return head
        while head:
            tmp=head.next
            head.next=None
            stack.insert(0,head)
            if tmp:
                head=tmp.next
                prev.next=tmp
                prev=tmp
            else:
                head=tmp
        while stack:
            prev.next=stack.pop()
            prev=prev.next
        return begin
