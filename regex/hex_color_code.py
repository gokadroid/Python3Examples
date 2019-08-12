# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
n = input()

for i in range(int(n)): #1

    line = input()

    z = re.findall(r".(#[0-9A-Fa-f]{6}|#[0-9A-Fa-f]{3})",line) #2

    for i in range(len(z)):
        print(z[i])
    
     
'''
(?< !^) means not match the start of each line, that how we erase #BED and #Cab

(?:[\da-f]{3}){1,2} , (?: ) means we don't store the message that match in the (), which ensure us to store the information in (# .....{1,2}). That's how non-capturing group works.

[\da-f]{3}{1,2} means [\da-f]{3} or [\da-f]{6}, and I guess the coder should have used the re.I in order to get the [A-F]
'''

'''
colour_regex=r'(?<!^)(#(?:[\da-f]{3}){1,2})'

n=int(input())
colours=[]
for _ in range(n):
    colours.append(re.findall(colour_regex, input()))

for i in range(len(colours)):
    print(colours[i])



'''
