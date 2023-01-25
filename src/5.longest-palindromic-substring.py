#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start


class Solution:
    def get_palindrone(self, s: str, left: int, right: int) -> str:
        """有効な範囲かつ左右の文字が一致する限りIndexを動かす"""
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # 最終的にleftは-1になりうるので+1
        # rightはIndexではなく文字数の指定が必要なので、そのままの値でよい
        left += 1
        return s[left:right]

    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            # 奇数の場合は、開始位置は中央値のIndex
            palindrome = self.get_palindrone(s, i, i)
            if len(longest) < len(palindrome):
                longest = palindrome
            # 偶数の場合は、中央値がないため開始位置を一つずらす
            palindrome = self.get_palindrone(s, i, i + 1)
            if len(longest) < len(palindrome):
                longest = palindrome
        return longest


# @lc code=end

s = Solution()
print("result:", s.longestPalindrome("babad"))
print("result:", s.longestPalindrome("cbbd"))
print("result:", s.longestPalindrome("aaaa"))
