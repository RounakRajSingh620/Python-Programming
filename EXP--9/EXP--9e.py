import functools 


lis = [
    1,
    3,
    5,
    6,
    2,
]
print("The product of list elements is : ", end="")
print(functools.reduce(operator.mul , lis))
print("The concatenated product is : ", end="")
print(functools.reduce(operator.add, ["welcome", "to", "SRM"]))
