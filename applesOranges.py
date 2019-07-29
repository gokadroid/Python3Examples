#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    applesCount=0
    orangeCount=0
    for i in range(0,len(apples)):
        if apples[i] > 0 and apples[i]+a >= s and apples[i]+a<=t:
            applesCount+=1
    for i in range(0,n):
        if oranges[i] < 0 and oranges[i]+b >= s and oranges[i]+b<=t:
            orangeCount+=1
    print(applesCount)
    print(orangeCount)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)


#Sam's house has an apple tree and an orange tree that yield an abundance of fruit. In the diagram below, the red region denotes his house, where  is the start point, and  is the endpoint. The #apple tree is to the left of his house, and the orange tree is to its right. You can assume the trees are located on a single point, where the apple tree is at point , and the orange tree is at #point .
#When a fruit falls from its tree, it lands  units of distance from its tree of origin along the -axis. A negative value of  means the fruit fell  units to the tree's left, and a positive value of  #means it falls  units to the tree's right.
#Given the value of  for  apples and  oranges, determine how many apples and oranges will fall on Sam's house (i.e., in the inclusive range )?
#For example, Sam's house is between  and . The apple tree is located at  and the orange at . There are  apples and  oranges. Apples are thrown  units distance from , and  units distance. Adding #each apple distance to the position of the tree, they land at . Oranges land at . One apple and two oranges land in the inclusive range
