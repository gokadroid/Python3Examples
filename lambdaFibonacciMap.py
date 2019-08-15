#https://www.hackerrank.com/challenges/map-and-lambda-expression/problem?h_r=next-challenge&h_v=zen
cube = lambda x: x*x*x# complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    fib=[]
    if n < 1:
        return []
    elif n==2:
        fib= [0,1]
    elif n==1:
        fib = [0]
    else:
        fib= [0,1]
        fib1=0
        fib2=1
        for i in range(2,n,1):
            fibsum=fib1+fib2
            fib.append(fibsum)
            fib1=fib2
            fib2=fibsum
    return fib

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
