import numpy
import math

matrix1 = numpy.array([[1,2,1],
                       [6,2,1],
                       [4,0,1]])

print(matrix1)

determinant = numpy.linalg.det(matrix1)

print(abs(int(determinant)))
print(abs(int(determinant/2)))


