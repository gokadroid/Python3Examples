#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    total=0
    max=0
    

    if len(arr)<1:
        return
    for item in arr:
        total+=item
    min=total
    for item in arr:
        if total-item >= max:
            max=total-item
        if total-item < min:
            min=total-item
    print(min, max)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
   
#Sample Input
#1 2 3 4 5
#Sample Output
#10 14

#Explanation
#Our initial numbers are , , , , and . We can calculate the following sums using four of the five integers:
#If we sum everything except , our sum is .
#If we sum everything except , our sum is .
#If we sum everything except , our sum is .
#If we sum everything except , our sum is .
#If we sum everything except , our sum is .
