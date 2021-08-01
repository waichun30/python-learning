from functools import partial


def multiply(x, y):
    return x * y


# create a new function that multiplies by 2
dbl = partial(multiply, 2)
print(dbl(4))

print()

#Following is the exercise, function provided:
from functools import partial
def func(u,v,w,x):
    print(u)
    print(v)
    print(w)
    print(x)
    return u*4 + v*3 + w*2 + x
#Enter your code here to create and print with your partial function

val = partial(func,0,0,20)

print(val(20))