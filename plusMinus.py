#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positive=0
    negative=0
    zero=0
    total=len(arr)

    if total == 0:
        print(0)
        print(0)
        print(0)
        return
  
    for item in arr:
        if item > 0:
            positive+=1
        elif item < 0:
            negative+=1
        else:
            zero+=1
    print(positive/total)
    print(negative/total)
    print(zero/total)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

#Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros. Print the decimal value of each fraction on a new line.
#Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.
#For example, given the array  there are  elements, two positive, two negative and one zero. Their ratios would be ,  and . It should be printed as
#0.400000
#0.400000
#0.200000
