from sympy import *

expr = cos(x) + 1
print(expr.subs(x, y))
x, y, z = symbols("x y z")
print(expr=x**y)
print(expr)
expr = sin(2 * x) + cos(2 * x)
print(expand_trig(expr))
print(expr.subs(sin(2 * x), 2 * sin(x) * cos(x)))
expr = x**4 - 4 * x**3 + 4 * x**2 - 2 * x + 3
replacements = [(x**i, y**i) for i in range(5) if i % 2 == 0]
print(expr.subs(replacements))
str_expr = "x**2 + 3*x - 1/2"
expr = sympify(str_expr)
expr
expr.subs(x, 2)
expr = sqrt(8)
print(expr.evalf())
expr = cos(2 * x)
expr.evalf(subs={x: 2.4})
one = cos(1) ** 2 + sin(1) ** 2
print((one - 1).evalf())
