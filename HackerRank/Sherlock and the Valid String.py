'''
Sherlock considers a string to be valid if all characters of the string appear the same number of times. 
It is also valid if he can remove just  character at  index in the string, and the remaining characters will occur the same number of times. 
Given a string , determine if it is valid. If so, return YES, otherwise return NO.

Function Description)

Complete the isValid function in the editor below. It should return either the string YES or the string NO.

isValid has the following parameter(s):

s: a string

Input Format)

A single string .

Constraints)

Each character
 
Output Format)

Print YES if string  is valid, otherwise, print NO.

Sample Input 0)

aabbcd

Sample Output 0)

NO

Explanation 0)

Given , we would need to remove two characters, both c and d  aabb or a and b  abcd, to make it valid. 
We are limited to removing only one character, so  is invalid.
'''

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict, Counter
# Complete the isValid function below.
def isValid(s):
    s = sorted(s) #알파벳 순서대로 정렬
    miss = 0 #다른 갯수가 나오면 이걸로 체크
    count = 0 #나와야하는 갯수(초깃값:0)
    cur = 1 #현재까지의 갯수
    prev = s[0]

    for st in s[1:]:
        # print("count:",count,"cur:", cur,"miss:", miss)
        if st == prev:
            cur += 1
        else:
            if count == 0:
                count = cur
            if count != cur:
                if miss == 0:
                    miss = cur
                else:
                    return 'NO'
            cur =1
            prev = st
    
    if count != cur and miss != 0:
        return  'NO'
    return 'YES'
                    
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
