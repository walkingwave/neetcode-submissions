class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #group all anagrams together
        #use a hash map 
        #key: sorted anagram, value: the container of all values 

        '''groups = {}

        word = "tea"
        key = "aet"  # Sorted letters of "tea"

        # If the key doesn't exist yet, start a new list for it
        if key not in groups:
        groups[key] = []

        #   Append the word to the list sitting at that key
        groups[key].append(word)'''

        #sorted() takes a word, and returns a list of its alphabetically sorted characters 
        #strategy: take each entry, use the sorted function 
        #make a new key with that sorted value 
        #every new word goes into that entry of the hash map

        groups = {}

        for word in strs:
            key = "".join(sorted(word))
            #check if the group does not exist 
            if key not in groups:
                groups[key] = [] # create new empty list
            groups[key].append(word) #add the new anagram to the group

        return list(groups.values()) #returns a list of lists containing values



