'''
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        right = head.next
        prehead = ListNode(0, head)
        left = prehead
        dupaccour = False
        while right:
            if right.val == left.next.val:
                dupaccour = True
                left = left
                if right.next == None:
                    left.next = None
            else:
                if dupaccour:
                    left.next = right
                    dupaccour = False
                else:
                    left = left.next
            right = right.next
        return prehead.next
