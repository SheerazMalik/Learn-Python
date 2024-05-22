#for loop is stupid servent because it return all values which store in iterable. example..  when you need one shirt from
# .. your almari then your servent give you all shirts. same like foor loop its not break. it return all values

a =[1,2,3,4,5]
print(type(a))
print(a)
for var_item in a:
    print(var_item)

#string
#One way just print all item list b

b = ["a","b","c","d","e"]
print(type(b))
print(b)
for var_item in b:
    print(var_item)    

#2nd way 
calculate_item = len(b)
print(calculate_item)
#now we have length of item which store in tuple, or list, or set or dictionary
#then next we used range function on length 
for var_item in range(calculate_item):
    print(b[var_item])

