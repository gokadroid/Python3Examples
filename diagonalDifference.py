#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    n=len(arr)
    sum=0
    dsum1=0
    dsum2=0
    for i in range(0,n):
        #print(arr[i][i],arr[i][n-1+i])
        dsum1+=arr[i][i]
        dsum2+=arr[i][n-1-i]
    if dsum1-dsum2<0:
        sum=-(dsum1-dsum2)
    else:
        sum=dsum1-dsum2
    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

#Given a square matrix of size , calculate the absolute difference between the sums of its
#diagonals.
#Input Format
#The first line contains a single integer, . The next lines denote the matrix's rows, with each line
#containing space-separated integers describing the columns.
#Constraints
#Output Format
#Print the absolute difference between the two sums of the matrix's diagonals as a single integer.
