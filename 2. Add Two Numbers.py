# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode

        test url :https://leetcode.com/problems/add-two-numbers/description/
        考察的是数据结构
        """
        l3 = ListNode(0)
        head = l3

        while True:
            if l1 == None:
                l1 = ListNode(0)
            if l2 == None:
                l2 = ListNode(0)

            tmp = l1.val + l2.val + l3.val
            if tmp > 9:
                tmp = tmp % 10
                l3.next = ListNode(1)

                l3.val = tmp
                l1 = l1.next
                l2 = l2.next
                l3 = l3.next
                if l1 == None and l2 == None:
                    break

            else:
                l3.val = tmp
                l1 = l1.next
                l2 = l2.next
                if l1 == None and l2 == None:
                    break
                l3.next = ListNode(0)
                l3 = l3.next

        return head


if __name__ == '__main__':
    l1 = ListNode(2)#[2, 4, 3]
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)#[5, 6, 4]
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    ex = Solution()
    result = ex.addTwoNumbers(l1,l2)

    while True:
        print(result.val)
        result = result.next
        if result == None:
            break

