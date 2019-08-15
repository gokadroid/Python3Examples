# Enter your code here. Read input from STDIN. Print output to STDOUT

#>>> s = set('HackerRank')
#>>> s.add('H')
#>>> print s
#set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])
#>>> print s.add('HackerRank')
#None
#>>> print s
#set(['a', 'c', 'e', 'HackerRank', 'H', 'k', 'n', 'r', 'R'])

if __name__ == '__main__':
    

    nm = int(input())

    s = set()

    for _ in range(nm):
        s.add(str(input()))

    print(len(s))
