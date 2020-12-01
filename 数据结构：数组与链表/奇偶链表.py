'''
给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。

请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/algorithm-and-interview-skills/xiq392/
来源：力扣（LeetCode）
'''
// 考察要点： 领头节点 oddhead and evenhead

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head:
            oddhead  = head
            evenhead = head.next
            odd = head
            even = head.next
            while even and even.next:
                odd.next = even.next
                odd = even.next
                even.next = odd.next
                even = odd.next
            odd.next = evenhead
            return oddhead
        else:
            return head
