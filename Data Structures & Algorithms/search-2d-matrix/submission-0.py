class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        #brute force 

 #       for row in matrix:
 #           if target in row:
 #               return True

 #           else:
 #               return False
        

#how to optimize in O(log(m*n)) time? 
#for log solutions, use binary search
# dont flatten the list with nums.append() because that takes O(n*m) time

        rows = len(matrix)
        cols = len(matrix[0])

        #binary search boundaries is number of entries in the matrix 
        
        right = rows*cols - 1
        left = 0 

        while left <= right:
            mid = (left+right) // 2

            #this indexing trick tells you which row and column mid is in 
            row = mid // cols
            col = mid % cols

            value = matrix[row][col]

            if value == target:
                return True
            
            if value > target:
                right = mid-1

            if value < target:
                left = mid+1

        return False

        #TC: O(log(m*n)) binary search with m*n elements
        #SC: O(1) not adding anything additional


        

