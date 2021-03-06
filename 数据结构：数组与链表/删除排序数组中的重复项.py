// 题目描述： 
'''给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

'''
//双指针
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 1
        n = len(nums)
        if(n<2):
            return n
        while(right < n):
            if(nums[left] == nums[right]):
                right += 1
            else:
                left += 1
                nums[left] = nums[right]
                right += 1
        return left + 1
