#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if (x2 > x1 and v2>= v1) or (x2<x1 and v2<= v1):
        return "NO"
    
    if x1>=x2:
        if ((x1 - x2) % ( v2 - v1) == 0):
            return "YES"
        else:
            return "NO"
    else:
        if ((x2 - x1) % ( v1 - v2) == 0):
            return "YES"
        else:
            return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()


#You are choreographing a circus show with various animals. For one act, you are given two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity).
#The first kangaroo starts at location  and moves at a rate of  meters per jump.
#The second kangaroo starts at location  and moves at a rate of  meters per jump.
#You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. If it is possible, return YES, otherwise return NO.
#For example, kangaroo  starts at  with a jump distance  and kangaroo  starts at  with a jump distance of . After one jump, they are both at , (, ), so our answer is YES.
#Function Description
#Complete the function kangaroo in the editor below. It should return YES if they reach the same position at the same time, or NO if they don't.
#kangaroo has the following parameter(s):
#x1, v1: integers, starting position and jump distance for kangaroo 1
#x2, v2: integers, starting position and jump distance for kangaroo 2
