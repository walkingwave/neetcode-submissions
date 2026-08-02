class Solution:

    def encode(self, strs: List[str]) -> str:

        #encode by giving num of characters + seperator + string

        #define encoded string first 
        encoded_string = ""

        for strn in strs:
            encoded_string += str(len(strn)) + '#' + strn #num of characters, then seperator, then stirng

        return encoded_string

    def decode(self, s: str) -> List[str]:

        res = []
        i = 0

        while i < len(s): #go through string 
            j = i 
            while s[j] != '#': #find location of delimiter 
                j += 1

            length = int(s[i:j])

            start_of_str = j+1 # letter after limiter is start of string 
            end_of_str = start_of_str + length # finds end of ther current string
            res.append(s[start_of_str:end_of_str]) #append to end of res (list)

            i = end_of_str

        return res

        #tc: O(n)
        #sc: O(n)
