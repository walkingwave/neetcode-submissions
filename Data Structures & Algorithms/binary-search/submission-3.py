class Solution:
    def search(self, nums: List[int], target: int) -> int:



        #nums is sorted in ascending order 
        
        if target not in nums:
            return -1

        #search must run in O(logn) time
        
        #have a mid, left, and right point 

        left = 0 
        right = len(nums) - 1 

        while left <= right:
            mid = (left+right)//2

            if target == nums[mid]: # taking index mid of nums to see if it matches the target
                return mid
                
            #change left and right depending on if target is lower or higher thna the midpoint
            # add 1 because we already checked mid
            if target > nums[mid]:
                left = mid+1

            if target < nums[mid]: 
                right = mid-1

        return -1

        #TC: O(logn)
        #SC: O(n)