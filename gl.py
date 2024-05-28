""" Here we will discuss global and local scope. when we declere variable in func then scope of this variable will be local. Even that we would not convert this scope into global
this local scope variable can access in nested function also. but if we want convert this into global then we used glbal keyword with this variable.
And if function outside of function block then func will be consider global which can acess at all space inside function outside function and whole file...  """

clothes="Dirty Clothes"


def washingmachine(cleanclothes):
    global clothes
    clothes = cleanclothes
    print(clothes)
    print(id(clothes))
print(clothes)
print(id(clothes))

washingmachine("Clean Clothes")
print(clothes)
print(id(clothes))
