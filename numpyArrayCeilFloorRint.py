import numpy, sys
numpy.set_printoptions(sign=' ')
arr = input().rstrip().split(' ')
my_array = numpy.array(arr).astype(float)


#print()
sys.stdout.write(str(numpy.floor(my_array)))
print()
sys.stdout.write(str(numpy.ceil(my_array)))
print()
sys.stdout.write(str(numpy.rint(my_array)))
#import numpy

#numpy.set_printoptions(sign=' ')

#a = numpy.array(input().split(),float)

#print(numpy.floor(a))
#print(numpy.ceil(a))
#print(numpy.rint(a))
