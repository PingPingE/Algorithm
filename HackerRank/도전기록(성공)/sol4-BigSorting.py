#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    unsorted = [ input() for _ in range(int(input()))]
    unsorted.sort(key= int)
    for s in unsorted:
        print(s)
