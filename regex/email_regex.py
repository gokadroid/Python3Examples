# Enter your code here. Read input from STDIN. Print output to STDOUT

'''
A valid email address meets the following criteria:

It's composed of a username, domain name, and extension assembled in this format: username@domain.extension
The username starts with an English alphabetical character, and any subsequent characters consist of one or more of the following: alphanumeric characters, -,., and _.
The domain and extension contain only English alphabetical characters.
The extension is 1,2,3 or  characters in length.
'''
import email.utils
import re

username='^[A-Za-z][A-Za-z-\.\_\d]+'
domain='@[A-Za-z]+'
extension='\.[A-Za-z]{1,3}'
n=int(input())

for _ in range(n):
    (name, email_id) = email.utils.parseaddr(input())
    if bool(re.match(username+domain+extension+'$', email_id)):
        #print(n)
        print(email.utils.formataddr((name, email_id)))
#('DOSHI', 'DOSHI@hackerrank.com')
#print email.utils.formataddr(('DOSHI', 'DOSHI@hackerrank.com'))
#DOSHI <DOSHI@hackerrank.com>
