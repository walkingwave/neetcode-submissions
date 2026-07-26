class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #hasmap stores key value pairs 
        #hash set only stores key-only values
        #hash set implemented wiht hash map with dummy/placeholder

        seen = set() 

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        
        return False