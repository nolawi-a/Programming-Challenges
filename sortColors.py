"""75. Sort Colors (MEDIUM)
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same 
color are adjacent, with the colors in the order red, white, and blue. We will use the integers 0, 1, and 2 to 
represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function."""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # We use a three pointer system to reduce the number of passes to 1
        zeroPntr, onePntr, twoPntr = 0, 0, len(nums) - 1
        while onePntr <= twoPntr:
            if nums[onePntr] == 0:
                nums[zeroPntr], nums[onePntr] = nums[onePntr], nums[zeroPntr]
                zeroPntr += 1
                onePntr += 1
            elif nums[onePntr] == 1:
                onePntr += 1
            else:
                nums[onePntr], nums[twoPntr] = nums[twoPntr], nums[onePntr]
                twoPntr -= 1
        return nums
