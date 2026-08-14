class Solution:
    def isPalindrome(self, s: str) -> bool:
        #strategy: have one pointer on the left and one on the right
        #have a while loop for while left < right 

        left = 0 
        right = len(s) - 1

        while left<right:
            
            #need to account for non-alphanumeric characters
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1
            
            #sets to lowercase for case insensitivity
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True