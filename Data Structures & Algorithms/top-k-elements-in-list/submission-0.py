class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #hashmap, key: integer k, value: frequency 
        #return list with k entries of the keys that have the highest value
        
        freqs = {}

        #first check if the key exists in the map yet

        for i, num in enumerate(nums): # if not, create it and add 1 
            if num not in freqs:
                freqs[num] = 1


            else:
                freqs[num] +=1

         # return list(freqs) - this returns every unique number, not the k == list(freqs.keys())

         #sort each key based on its frequency, you get the value with the .get function
         #list slicing [:k] means you only take the first k terms 
         #need to reverse because by default itll sort least to most frequent
        return sorted(freqs, key=freqs.get, reverse=True)[:k]    


#tc: goes through entire list once, and then sorts it once so O(n + mlogm), worst case m = n so O(nlogn)
#typical sort, m per level, logm levels = mlogm
#sc: O(n)



    