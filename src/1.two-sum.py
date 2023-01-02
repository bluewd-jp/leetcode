from typing import List

#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = []
        for i in range(len(nums)):
            n = target - nums[i]
            if n in l:
                return [l.index(n), i]
            else:
                l.append(nums[i])
        return [0, 0]


# @lc code=end
