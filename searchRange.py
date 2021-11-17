"""Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity."""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums) - 1
        start = -1
        # Use binary search to find the first instance of our target
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                start = mid
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
                
        if start == -1:
            return [-1,-1]
        
        # Use binary search to find the last instance of our target
        # We set low to start because there's no need to consider elements before
        #  the first instance of target
        low, high = start, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                end = mid
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
        return [start, end]
            
