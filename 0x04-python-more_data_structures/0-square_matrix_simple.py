#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
<<<<<<< HEAD
	if not matrix:
		print()
	return [list(map((lambda x: x * x), i)) for i in matrix]
=======
	return [list(map((lambda x: x ** 2), i)) for i in matrix]
>>>>>>> e56c39b809e0bbe05783c71e909112b41fdaa6b2
