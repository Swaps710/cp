# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack=[]
        while head:
            stack.append(head.val)
            head=head.next
        i=0
        j=len(stack)-1
        flag=True
        while(i<j):
            if(stack[i]!=stack[j]):
                flag=False
                break
            i+=1
            j-=1
        return flag
        
