#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    
    n=len(s)
    hr=s[0:2]
    pm=s[n-2]
    print(hr, pm)

    if (pm == "P") or (pm == "p"):
        if hr == "12":
            return s[0:n-2]
        else:
            return str(int(hr)+12)+s[2:n-2]
    elif pm == "A" or pm == "a":
        if hr == "12":
            return "00"+s[2:n-2]
        else:
            return s[0:n-2]
    else:
        return

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()

#Given a time in -hour AM/PM format, convert it to military (24-hour) time.
#Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.
#Function Description
#Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.
#timeConversion has the following parameter(s):
#s: a string representing time in  hour format
