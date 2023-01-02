from typing import Optional

#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @lc code=start
# Definition for singly-linked list.
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return None
        elif l1 is None:
            return l2
        elif l2 is None:
            return l1
        else:
            sum = l1.val + l2.val
            if sum < 10:
                return ListNode(val=sum, next=self.addTwoNumbers(l1.next, l2.next))
            else:
                return ListNode(
                    val=sum - 10,
                    next=self.addTwoNumbers(
                        self.addTwoNumbers(l1.next, ListNode(1)), l2.next
                    ),
                )


# @lc code=end
