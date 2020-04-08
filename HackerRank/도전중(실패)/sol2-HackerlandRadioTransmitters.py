#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n,k = map(int, input().split())
    x = list(map(int, input().rstrip().split()))
    x.sort()
    cnt = 0
    res = 0
    bet = list(x[i+1]-x[i] for i in range(n-1))
    for i in range(len(bet)):#집들 사이의 거리
        if cnt+bet[i]>=(2*k+1):
            res+=1
            cnt = bet[i]
            if cnt+bet[i] == (2*k+1):
                cnt = 0
        else:
            if i == len(bet)-1:
                res += 1
            else:
                cnt += bet[i]
    print(res)   
