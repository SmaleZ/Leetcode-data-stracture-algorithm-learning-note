'''
题目描述：给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
'''
//哈希表+数组前缀，这里是用python 的dictionary 类型代替哈希表实现
//代码：
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subSum = {}
        subSum.update({0 : 1})
        presum = 0
        res = 0
        for num in nums:
            presum += num
            if(presum-k in subSum):
                res += subSum[presum-k]
            if(presum in subSum):
                subSum.update({presum : subSum[presum]+1})
            else:
                subSum.update({presum : 1})
        
        return res
