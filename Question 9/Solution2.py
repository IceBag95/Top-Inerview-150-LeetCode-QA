'''
SOLUTION 2 BASED ON THE EXPLANATION'S APPROACH

In this solution we find the SHORTEST path if there is one to our goal and return True.
If none is found we return False.


We start from the target (like finding the correct path to a maze) and go back trying to find the furthest away 
from the end position, with a jump value that will at least reach the end of the array. 
If that position is not the starting position, we do the same again as many times needed to reach the beginning 
of the array but now we try to reach the last found position.
At some point we will reach the beginning and that is the most efficient path.
If at some point we can't find a value that reaches our goal, we return False.
If the path is found then we return True. 

The commented lines are there just to show the Shortest path to our goal
Feel free to uncomment those lines to see the path. 
'''


def canJump(nums: list[int]) -> bool:

    N = len(nums)
    l = N-1
    #print(nums)
    #m = []

    def findnextpos(arr, l_idx):

        pos = l_idx
        i = l_idx - 1
        while i >= 0:  

            if i+arr[i] >= l_idx and i < pos:
                pos = i 
            
            i -= 1
        
        if pos == l_idx:
            return -1
        
        return pos

    while l > 0:
        l = findnextpos(nums, l)
        if l ==  -1:
            return False
        #m.append(nums[l])
    
    #m.reverse()
    #print(m)
    return True


    


print(canJump([2,3,1,1,4]))






