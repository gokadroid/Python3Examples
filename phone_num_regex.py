# Enter your code here. Read input from STDIN. Print output to STDOUT 789
import re
n = int(input())

for _ in range(n):
    if bool(re.match(r'^[789]\d{9}$', input())):
        print("YES")
    else:
        print("NO")
