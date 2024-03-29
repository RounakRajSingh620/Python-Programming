from pyDatalog import pyDatalog
pyDatalog.create_terms('N,X0,X1,X2,X3,X4,X5,X6,X7')
pyDatalog.create_terms('ok,queens,next_queen')
queens(X0) <= (X0._in(range(8)))
queens(X0, X1) <= queens(X0) & next_queen(X0, X1)
queens(X0, X1, X2) <= queens(X0, X1) & next_queen(X0, X1, X2)
queens(X0, X1, X2, X3) <= queens(X0, X1, X2) & next_queen(X0, X1, X2, X3)
queens(X0, X1, X2, X3, X4) <= queens(
    X0, X1, X2, X3) & next_queen(X0, X1, X2, X3, X4)
queens(X0, X1, X2, X3, X4, X5) <= queens(
    X0, X1, X2, X3, X4) & next_queen(X0, X1, X2, X3, X4, X5)
queens(X0, X1, X2, X3, X4, X5, X6) <= queens(
    X0, X1, X2, X3, X4, X5) & next_queen(X0, X1, X2, X3, X4, X5, X6)
queens(X0, X1, X2, X3, X4, X5, X6, X7) <= queens(X0, X1, X2, X3,
                                                 X4, X5, X6) & next_queen(X0, X1, X2, X3, X4, X5, X6, X7)
next_queen(X0, X1) <= queens(X1) & ok(X0, 1, X1)
next_queen(X0, X1, X2) <= next_queen(X1, X2) & ok(X0, 2, X2)
next_queen(X0, X1, X2, X3) <= next_queen(X1, X2, X3) & ok(X0, 3, X3)
next_queen(X0, X1, X2, X3, X4) <= next_queen(X1, X2, X3, X4) & ok(X0, 4, X4)
next_queen(X0, X1, X2, X3, X4, X5) <= next_queen(
    X1, X2, X3, X4, X5) & ok(X0, 5, X5)
next_queen(X0, X1, X2, X3, X4, X5, X6) <= next_queen(
    X1, X2, X3, X4, X5, X6) & ok(X0, 6, X6)
next_queen(X0, X1, X2, X3, X4, X5, X6, X7) <= next_queen(
    X1, X2, X3, X4, X5, X6, X7) & ok(X0, 7, X7)
ok(X1, N, X2) <= (X1 != X2) & (X1 != X2+N) & (X1 != X2-N)
print(queens(X0, X1, X2, X3, X4, X5, X6, X7).data[0])
