class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        
        #use two hashmaps to store the count of each character

        seen_s, seen_t = {}, {}

        if len(s) != len(t): #anagrams must be the same length
            return False 

        for char in s: # create hashmap for s
            seen_s[char] = seen_s.get(char, 0) + 1 

        
        for char in t: #create hashmap for t
            seen_t[char] = seen_t.get(char, 0) + 1 

        return seen_s == seen_t #if hashmaps are the same they have the same quantities