class Solution:
    def climbStairs(self, n: int) -> int:
        
        #can climb 1 or 2 stairs at a time

        #if there are only 1 or 2 steps, return 1 or 2 

        if n <= 2:
            return n 

        prev1 = 2
        prev2 = 1
        #next is the dp step 
        #keep track of the last two steps to reach i, isnce there are two ways

        for i in range(3, n+1): #since range does not include n+1, only includes n 

            current = prev1+prev2  #steps fro current is the sum of both of the other steps
            prev2 = prev1 
            prev1 = current 

        return prev1

        #tc = O(n)
        #tc = O(1)

            

