# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        

        # algorithm for this habing a pointer for next node and next next node
        #if they are ever on the same node it is a loop (fast/slow pointer)

        #have a set to track which nodes youve seen 
        #if the node you are currently on is in the set then you are in a loop 


        seen = set()

        current = head

        while current:
            if current in seen:
                return True 

            else:
                seen.add(current)

            current = current.next

        return False



