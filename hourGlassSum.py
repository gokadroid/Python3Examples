#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    max=-63
    #index=0
    #print(len(arr))
    if len(arr)<3:
        return 0
    for j in range(1,len(arr)-1,1):
        for i in range(1,len(arr)-1,1):
            sum=0
            sum=arr[j-1][i-1]+arr[j-1][i]+arr[j-1][i+1] + arr[j][i]+arr[j+1][i-1]+arr[j+1][i]+arr[j+1][i+1]
            if sum >= max:
                #index=i
                max=sum
    return max

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
