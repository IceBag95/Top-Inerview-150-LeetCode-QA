class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if k < 0:
            return 'Iteration number should be non-negative'
        if k == 0:
            return nums

        for i in range(k):
            rotated_value = nums.pop()
            nums.insert(0, rotated_value)
        
        return nums
        