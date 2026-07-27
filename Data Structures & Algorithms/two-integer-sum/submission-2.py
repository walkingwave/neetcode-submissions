class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #use a hash map for two sum
        #key: number, value: index in the array 
        '''enumerate() is a built-in Python function that takes a 
        list (or any sequence) and hands you back two things on 
        every loop iteration: the index and the value at that index.'''

        seen = {}
        
        #needed number = target - current number
        #check hash map to see if we already stored that number 
        #walk through array one by one

        for i, num in enumerate(nums):

            needed = target - num

            if needed in seen: #name of the key is the key
                return [seen[needed], i] #returns prev_index, current_index

            #after checking if it was seen, if its not seen u need to add 
            #it to he hashmap 

            seen[num] = i #remember the index is the value


    #time complexity: O(n) + O(1) (checking hashmap + other ops are all O(1)) = O(n)
    #space complexity: O(n)