#!/bin/python3

import math
import os
import random
import re
import sys

def sol(arr):
    return [a for a in sorted(arr, key= lambda x: [len(x),x])]#각 숫자의 길이 정보 추가
if __name__ == '__main__':
    unsorted = [ input() for _ in range(int(input()))]
    for s in sol(unsorted):
        print(s)

#드디어 성공!!
#하지만 discussions를 참고했다. 그래도 다양한 사람들의 의견, 코드 등을 보면서 많이 배웠다.
#컴터가 더 연산을 쉽고 빠르게 할 수 있도록 더 많은 정보를 주자!
