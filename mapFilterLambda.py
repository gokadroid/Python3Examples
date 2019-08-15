#Use map, lambda and filter
# Create a list
#>> l = list(range(10))
#
# Create a lambda
#>> l = list(map(lambda x:x*x, l))
#
# Create a filter 
#>> l = list(filter(lambda x: x > 10 and x < 80, l))

#https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def fun(s):
    # return True if s is a valid email, else return False
    import re

    username='^[A-Za-z][A-Za-z-\_\d]+'
    domain='@[A-Za-z0-9]+'
    extension='\.[A-Za-z]{1,3}'
    return bool(re.match(username+domain+extension+'$', s))

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
