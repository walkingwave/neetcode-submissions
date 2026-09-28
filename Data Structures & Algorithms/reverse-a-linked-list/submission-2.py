# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        current = head 

        while current is not None: 
            next_node = current.next  # sets to next entry
            current.next = prev # makes the node point to whats behind current
            prev = current #moves prev up one 
            current = next_node # moves current up one 
    
        return prev

#tc = O(n) 
#sc = O(1)

        