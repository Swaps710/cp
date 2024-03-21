# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack=[]
        while head:
            stack.append(head)
            head=head.next
        temp=ListNode()
        dummy=temp
        while stack:
            temp.next=stack.pop()
            temp=temp.next
        temp.next=None
        return dummy.next
        
