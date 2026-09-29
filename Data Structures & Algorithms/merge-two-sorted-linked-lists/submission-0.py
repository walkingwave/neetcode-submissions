# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode() # parentheses -> create instance of a class

        current = dummy # dummy conitnues pointing at the start of the sorted merged list

        while list1 is not None and list2 is not None:
            if list1.val >= list2.val:
                current.next = list2 
                list2 = list2.next

            else: 
                current.next = list1
                list1 = list1.next

            current = current.next
        
        if list1 is not None:
            current.next = list1
        else: 
            current.next = list2

        

        return dummy.next


#tc = O(n+m) worst case go through entirety of both lists
#sc = O(1)- dummy is a helper node

