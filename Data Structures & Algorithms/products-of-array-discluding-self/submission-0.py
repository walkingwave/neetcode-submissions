class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #multiply by every single value in nums, then divide by nums[i]
        #what if nums[i] is 0? also says can you solve it without division operator 
        #product of all nums left of i x product of all to the right 

        prod_left = []
        prod_right = []

        all_prod = []
        curr =1

        for n in nums: #append to list fo each n 
            prod_left.append(curr)
            curr*=n

        curr =1 

        for n in reversed(nums): # same thing with reverse
            prod_right.append(curr)
            curr*=n

        prod_right.reverse() # flip it so index matches
        # combine the left and right 

        for l, r in zip(prod_left, prod_right):
            all_prod.append(l * r)

        return all_prod

        #tc: O(n)
        #sc: O(n), O(n) extra space here

        #can optimize this by making prod the output array and multiplying in place -> O(1) extra space, no need for prod left or right arrays, just have one array for everything
        '''range(start, stop, step) — here it's range(n-1, -1, -1).

start = n - 1: the last valid index of the array (since indices go from 0 to n-1)
stop = -1: it stops before reaching -1 (range's stop is always exclusive), so it actually goes all the way down to and includes 0
step = -1: count downward, one at a time'''