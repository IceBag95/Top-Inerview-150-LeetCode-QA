class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    
        merged_arr = []
        

        while len(nums1) > 0 and len(nums2) > 0:
            if nums1[0] < nums2[0]:
                merged_arr.append(nums1.pop(0))    
            else:
                merged_arr.append(nums2.pop(0))

        if len(nums1) > 0:
            merged_arr += nums1
        
        if len(nums2) > 0:
            merged_arr += nums2
        

        L = len(merged_arr)
        
        if L % 2 == 0:
            median = (merged_arr[(L // 2) - 1] + merged_arr[L // 2]) / 2
        else:
            median = merged_arr[L // 2]  
        
        return median
    