# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        #iterate through true, and swap self.left with self.right
        #need a way to traverse through tree. Use a stack for DFS or a queue for BFS


        if root is None:
            return None

        stack = [root]
       

        while stack:

            current = stack.pop()
            
            temp = current.left 

            current.left = current.right
            current.right = temp 
            

            if current.left:
                stack.append(current.left)

            if current.right:
                stack.append(current.right)    

        return root

        #tc = O(n)
        #sc = O(n)
        
            

        