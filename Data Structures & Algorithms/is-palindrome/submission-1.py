class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        #pointer at first and last index, at each increment check if they are equal to each other

        # chars = list(s)
        # first = chars[0]
        # last = reversed(chars[0])

        # for i in range(len(s)//2):
        #     if first[i]!=last[i]:
        #         return False

        # return True
        # this doesnt work because chars[0] is a single char, and need to ignore non alphanumeric charactes


        left = 0 #left pointer
        right = len(s)-1 #right pointer 

       
        while left <= right: 

            # Skip non-letter/non-number characters on the left
            if not s[left].isalnum():
                left += 1
                continue

            # Skip non-letter/non-number characters on the right
            if not s[right].isalnum():
                right -= 1
                continue


            if s[left].lower() == s[right].lower():
                left+=1
                right-=1 

            else: 
                return False

        return True

