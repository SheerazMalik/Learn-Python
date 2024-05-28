

def recursive_fun(n):
    if n<=1:
        # print(f"i am at if statment {n}")
        return 1
    else:
        # print(n)
        # print(id(n))

        a = n * recursive_fun(n-1)

        # print(recursive_fun(n-1))
        # print(a)
        # print(type(a))
        # print(id(a))
        # print(f"i am N {n}")

        return a
    
print(recursive_fun(5))