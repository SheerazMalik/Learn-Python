#Sets
#sets always in curly braces.
#Sets return one value no matter how many   value exist 
#Set add() used for adding value or item in set. but set add value on its own choice because its unordered.


A={"a","b","b","c","a","d",}
B={2,0,8,6,7,9,2,4,10,"a","c","a","b",}

# print(A)
# print(B)
print(A.intersection(B))
print(A.union(B))
A.add("xxx")
print(A)