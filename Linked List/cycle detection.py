# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#2 pointers
class Solution(object):
    def hasCycle(self, head):
        fast = head
        while fast and fast.next :     
            fast = fast.next.next
            head = head.next
            if head is fast :
                return True 
        return False
