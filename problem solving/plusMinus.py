#!/bin/python3

#Given an array of integers, calculate the ratios of its elements
#that are positive, negative, and zero.
#Print the decimal value of each fraction
#on a new line with  places after the decimal.

import math
import os
import random
import re
import sys

#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    plus = 0
    minus = 0 
    zero = 0
    for i in arr:
        if i<0:
            minus += 1
        elif i>0:
            plus += 1
        else:
            zero += 1
    n = len(arr)
    print(round(plus/n, 6))
    print(round(minus/n, 6))
    print(round(zero/n, 6))
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
