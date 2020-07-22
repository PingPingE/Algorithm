'''
234. Palindrome Linked List
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
''''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#80 ms	24 MB
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        target = []
        if head is None:
            return True
        while True:
            target.append(head.val)
            if head.next == None:
                break
            head = head.next
 
        s,e =0,len(target)-1
        while s<e:
            if target[s] == target[e]:
                s+=1
                e-=1
            else:
                return False
        return True