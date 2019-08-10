#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    #https://stackoverflow.com/questions/2241891/how-to-initialize-a-dict-with-keys-from-a-list-and-empty-value-in-python
    dict = {key: 0 for key in queries if key }
    
    for myString in strings:
        if myString in dict.keys():
            dict[myString]+=1
    myResult=[]
    #print(dict)
    for key in queries:
        myResult.append(dict[key])
    return myResult

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)
    #matchingStrings(strings, queries)
    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
