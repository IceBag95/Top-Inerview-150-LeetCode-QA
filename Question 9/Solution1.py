'''
SOLUTION 1

In this solution we are not bothered to find the most efficient way to the end of the array if there is one. 
We just want to find a valid path and if we can the function returns True, else it returns False.

So we start from the 0 position. We want to push as far away from our current position as possible,
keeping in mind NOT to land on a 0 (we won't be able to move again from there) or out of bounds.

This is a beginner friendly approach but is NOT the way the explanation of the examples / cases
show us how to find a path. Still it passes the tests as the goal is reached. 
'''


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        N = len(nums)
        f = 0


        if nums[f] == 0:
            return False

        while f < N:

            max_jump = nums[f]
            target_pos = f + max_jump

            while target_pos >= N or nums[target_pos] == 0:
                
                target_pos -= 1
                
                if target_pos == N:
                    return True
                
                if target_pos == f:
                    return False
            
            f = target_pos

  
