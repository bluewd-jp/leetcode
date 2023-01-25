#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        l = len(nums)

        if l % 2 == 0:
            i = int(l / 2) - 1
            j = int(l / 2)
            return (nums[i] + nums[j]) / 2
        i = int(l / 2)
        return nums[i]


# @lc code=end
