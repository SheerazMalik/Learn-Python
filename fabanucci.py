#here we discuss fabanucci function but this is not good its take a heavy computational power...
def fab(n):
    if n<2:
        return n
    else:
        return fab(n-1)+fab(n-2)
    
for i in range(100):
    print(i,fab(i))