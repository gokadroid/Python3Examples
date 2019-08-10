#learn how to print in one line
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    c=[]
    index=d%n
    for i in range(index,n,1):
        print(a[i], end=" ")
    for i in range(0,index,1):
        print(a[i], end=" ")
