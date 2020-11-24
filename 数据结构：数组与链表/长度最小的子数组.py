//给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。

//双指针解法
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        right = 0
        left = 0
        total = 0
        n = len(nums)
        minLen = n + 1
        while (right < n):
            total += nums[right]
            while (total >= s):
                minLen = min(right - left + 1, minLen)
                total -= nums[left]
                left += 1
            right += 1 
        if minLen == n + 1:
            return 0
        return minLen
