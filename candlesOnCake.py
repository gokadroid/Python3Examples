#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    max=0
    count=0

    if len(ar)<1:
        return
    for item in ar:
        if item > max:
            max=item
            count=1
        elif item == max:
            count+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()


#You are in-charge of the cake for your niece's birthday and have decided the cake will have one candle for
#each year of her total age. When she blows out the candles, she’ll only be able to blow out the tallest
#ones.
#For example, if your niece is turning years old, and the cake will have candles of height , , , , she
#will be able to blow out candles successfully, since the tallest candle is of height and there are such
#candles.
#Complete the function Given the height of each individual candle, find and print the number of candles
#she can successfully blow out.

#Sample Input 0
#4
#3 2 1 3
#Sample Output 0
#2
#Explanation 0
#We have one candle of height , one candle of height , and two candles of height . Your niece only
#blows out the tallest candles, meaning the candles where . Because there are such candles,
#we print on a new line.
