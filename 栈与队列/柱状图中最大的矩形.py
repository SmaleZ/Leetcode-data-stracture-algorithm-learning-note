#给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

#求在该柱状图中，能够勾勒出来的矩形的最大面积。

#知识点：单调栈，数组

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        if n<=0:
            return 0
        else:
            left_min = [0] * n
            right_min = [n] * n

            task_stack = list()

            for i in range(n):
                while task_stack and heights[i] <= heights[task_stack[-1]]: #如果当前枚举到的数小于单调栈中的数，则将单调栈中的数pop
                    right_min[task_stack[-1]] = i                           #如果此时单调栈pop,那么该数的右边最临近比它小的数就是当前枚举的数
                    task_stack.pop()
                left_min[i] = task_stack[-1] if task_stack else -1          #左边最邻近比它小的数是单调栈的末尾
                task_stack.append(i)
            
            area = [(right_min[i] - left_min[i] - 1) * heights[i] for i in range (n)]
            print (area)
            return max(area)



        
