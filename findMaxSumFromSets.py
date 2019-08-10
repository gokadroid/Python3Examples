#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    
    arr=n*[0]
    print(arr[n-1])
    max=0
    currentSum=0
    for i in range(0,len(queries),1):
        #print(queries[i][0]-1, end=" ")
        #print(queries[i][1]-1,  end=" ")
        #print(queries[i][2])
        arr[queries[i][0]-1] += queries[i][2] 
        if queries[i][1]+1 <= n:
            arr[queries[i][1]] -= queries[i][2] 
    
    print(arr)    
    for i in range(0,n,1):
        currentSum+=arr[i]
        #print(currentSum, end=" ")
        #print(max)
        if max < currentSum:
            max=currentSum
    #print(dict)
    #key_max = max(dict.keys(), key=(lambda k: dict[k]))
    #key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))

    return max

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
