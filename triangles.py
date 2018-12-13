import math
def hypotenuse(a,b):
    "'Give you a hypotenuse of a right triangle.'"
    hyp = math.sqrt(a**2 + b**2)
    return hyp

print(hypotenuse(3,4))