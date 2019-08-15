 #!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    myString=list(s)
    myStack=[]
    print(myString)
    for i in range(len(myString)):
        if myString[i] in ['{', '(', '[']:
            myStack.append(myString[i])
        elif myString[i] in ['}', ')', ']']:
            if len(myStack) < 1:
                return "NO"
            opening = myStack.pop()
            if (opening == '[' and  myString[i] == ']') \
            or (opening == '{' and  myString[i] == '}') \
            or (opening == '(' and  myString[i] == ')' ):
                print(opening, myString[i])
                continue
            else:
                return "NO"
    
    if len(myStack) < 1:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
