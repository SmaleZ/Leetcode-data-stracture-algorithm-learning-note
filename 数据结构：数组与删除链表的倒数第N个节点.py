'''
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？

'''
//知识点： 链表， 快慢指针， 带头结点
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        prehead = ListNode(0, head)
        first = head
        second = prehead

        for i in range(n):
            first = first.next
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return prehead.next
