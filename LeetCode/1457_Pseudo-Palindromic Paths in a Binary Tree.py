'''
Given a binary tree where node values are digits from 1 to 9. 
A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.

Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

Input: root = [2,3,1,3,1,null,1]
Output: 2 
Explanation: The figure above represents the given binary tree. 
There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. 
Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) 
and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#sol1:656 ms 49.2 MB
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        
        def is_palindrome(target):
            counter = Counter(target)
            c_len = len(list(filter(lambda x: x%2 == 1, counter.values()))) 
            # print(c_len)
            return True if c_len<=1 else False
        
        que = deque()
        que.append(([root.val],root))
        cnt = 0
        while que:
            cur_list, current = que.popleft()
            # print(cur_list)
            if current.left is None and current.right is None: #leaf노드면
                if is_palindrome(cur_list[:]):
                    cnt += 1
                continue
                
            if current.left:
                cur_list.append(current.left.val)
                que.append((cur_list[:], current.left))
                cur_list.pop()
                
            if current.right:
                cur_list.append(current.right.val)
                que.append((cur_list[:], current.right))
                cur_list.pop()
        return cnt