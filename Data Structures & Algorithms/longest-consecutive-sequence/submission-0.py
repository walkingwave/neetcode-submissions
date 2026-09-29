class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # nums.sort() -> dont sort array aim for O(n) time

        consecutive = 0


        num_set = set(nums)

        for num in num_set:
            if num-1 not in num_set:

                #then you are at the start of a consecutive sequence 
                start = num
                consec = 1 
                while start+1 in num_set:

                    
                    consec+=1
                    start+=1

            
                if consec > consecutive:
                    consecutive = consec

        return consecutive

#tc O(n) - for loop, placing in set
#sc O(n) - set