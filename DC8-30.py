import numpy

matrix1 = numpy.array([[1,3],
                        [2,5]])

print("Numpy Matrix is:")
print(matrix1)

determinant = numpy.linalg.det(matrix1)

print("\nDeterminant of given 2X2 matrix:")
print(int(determinant))