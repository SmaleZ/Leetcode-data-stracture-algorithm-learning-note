'''
给定一个增序排列数组 nums ，你需要在 原地 删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。


'''
 

//知识点：双指针

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j, count = 1, 1

        for i in range(1, len(nums)):
            if (nums[i] == nums[i-1]):
                count+=1
            else:
                count = 1
            if count <= 2:
                nums[j] = nums[i]
                j += 1
        return j
        
 #解法比较巧妙，个人尝试多次未果，原本想仿照之前删除排序数组重复项的方法来解决，但是没有成功。
