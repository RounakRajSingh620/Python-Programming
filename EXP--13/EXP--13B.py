from sympy.matrices import Matrix

m = Matrix([[1, 2, 3], [2, 3, 1]])
print(m)
M = Matrix(2, 3, [10, 40, 30, 2, 6, 9])
print(M)
print(M.shape)
print(M.row(0))
M.col(1)
M.row(1)[1:3]
print(M)
M = Matrix(2, 3, [10, 40, 30, 2, 6, 9])
M.col_del(1)
a = Matrix([[1, 2, 3], [2, 3, 1]])
print(a)
a1 = Matrix([[10, 30]])
a = M.row_insert(0, M1)
print(a)
a2 = Matrix([40, 6])
a = M.col_insert(1, M2)
print(a)
M1 = Matrix([[1, 2, 3], [3, 2, 1]])
M2 = Matrix([[4, 5, 6], [6, 5, 4]])
print(M1 + M2)
M1 = Matrix([[1, 2, 3], [3, 2, 1]])
M2 = Matrix([[4, 5], [6, 6], [5, 4]])
print(M1 * M2)
