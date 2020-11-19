#例题：斐波那契数

#方法一：递归
#代码：
class Solution:
    def fib(self, N):
        if (N == 0):
            return 0
        if (N ==1 or N == 2):
            return 1
        else:
            return self.fib(N -1) + self.fib(N - 2)
'''
复杂度分析
时间复杂度：O(2^N)O(2N)。这是计算斐波那契数最慢的方法。因为它需要指数的时间。
空间复杂度：O(N)O(N)，在堆栈中我们需要与 N 成正比的空间大小。该堆栈跟踪 fib(N) 的函数调用，随着堆栈的不断增长如果没有足够的内存则会导致 StackOverflowError。
'''
#例题：搜索插入位置

#方法：二分查找
#代码
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if(nums == None):
            return 0
        else:
            start = 0
            end = len(nums) - 1
            while(start <= end):
                mid =int((start + end) / 2)
                if(nums[mid] == target):
                    return mid
                elif(nums[mid] < target):
                    start = mid + 1
                else:
                    end = mid -1
            return start
'''
复杂度分析

时间复杂度：O(\log n)O(logn)，其中 nn 为数组的长度。二分查找所需的时间复杂度为 O(\log n)O(logn)。

空间复杂度：O(1)O(1)。我们只需要常数空间存放若干变量。
'''
