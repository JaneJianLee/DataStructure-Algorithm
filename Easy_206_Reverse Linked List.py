# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr = head
        prev = None
        temp = curr
        
        while curr is not None:
            curr = curr.next
            temp.next = prev
            prev = temp
            temp = curr
            
        return prev
