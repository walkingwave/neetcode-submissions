class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #hash set wont work here because it can only track if its seen
        #a has map can map the number of times its seen to the letter ( key value pair)

        #make a hash map for s and t and check if theyre equal to each other 

        #first check if the letters are the same as each other 

        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            # checks the key s[i], then gets the value. if no value returns default value (0). after adds 1 
            countT[t[i]] = countT.get(t[i], 0) + 1

        return countS == countT