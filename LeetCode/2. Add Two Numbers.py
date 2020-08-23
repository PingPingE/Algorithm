'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#sol1) linked list를 순서대로 순회하며 deque에 appendleft로 담아서 뒤집고 연산/연산 결과를 뒤집은 순서대로 ListNode에 연결한다. 104 ms 14.1 MB
from collections import deque
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        deq1,deq2 = deque(),deque()
        while l1:
            deq1.appendleft(l1.val)
            l1 = l1.next
    
        n1 = ''.join(map(str,list(deq1)))
        
        while l2:
            deq2.appendleft(l2.val)
            l2 = l2.next
        
        n2=''.join(map(str,list(deq2)))
        
        result = list(str(eval(f"{n1}+{n2}"))[-1::-1])
        
        res_Node = ListNode(result[0])
        tmp = res_Node
        for i in range(1,len(result)):
            tmp.next= ListNode(result[i])
            tmp = tmp.next

        return res_Node
            
#sol2) 낮은 자릿수부터 연산하면서 바로 ListNode에 연결한다. 68 ms 14 MB
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res_node = ListNode()
        cur_node= res_node
        sum,carry= 0, 0 #각 자리의 덧셈 결과, 자리올림수
        while l1 or l2:
            sum = carry+(l1.val if l1 else 0)+(l2.val if l2 else 0)
            carry = sum//10 
            cur_node.next = ListNode(val = sum%10)
            cur_node = cur_node.next
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        if carry: #마지막 연산(가장 높은 자릿수의 연산)에서 자리올림수가 1인 경우
            cur_node.next = ListNode(val = carry)
        return res_node.next
        