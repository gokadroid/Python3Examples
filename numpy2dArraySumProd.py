import numpy


nm = input().split()
n = int(nm[0])
m = int(nm[1])
numbers = []
for i in range(0,n,1):
    numpy.set_printoptions(sign=' ')
    arr = input().rstrip().split(' ')
    for j in range(0, len(arr),1):
        arr[j] = int(arr[j])
    numbers.append(arr)

#my_array = numpy.array(arr).astype(int)
my_array = numpy.array(numbers)
print(numpy.prod(numpy.sum(my_array, axis = 0), axis=0))
