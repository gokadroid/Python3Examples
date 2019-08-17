#!/bin/python3

import math
import os
import random
import re
import sys


#https://caisbalderas.com/blog/iterating-with-python-lambdas/

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

y = max([len(v) for v in matrix ])
myString=""
for column in range(y):
    for row in range(n):
        myString+=matrix[row][column]

print(myString)
print(re.sub("[^A-Za-z0-9]"," ",myString))
