#!/bin/python3

import math
import os
import random
import re
import sys
#Given five positive integers, find the minimum and maximum values
#that can be calculated by summing exactly four of the five integers.
#Then print the respective minimum and maximum values as a single line
#of two space-separated long integers.

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr.sort()
    minValue = arr[0] + arr[1] + arr[2] + arr[3]
    maxValue = arr[1] + arr[2] + arr[3] + arr[4]
    print(minValue, end=" ")
    print(maxValue)



if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
