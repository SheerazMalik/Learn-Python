#**List**
#Sequence of element called list 
#we can store element, list, and different data types in list e.g

var_list = ["a","b","c",[1,2,3],"z","y"]
print(var_list)
#indexing

print(var_list[1])

print(var_list[0:4])

print(var_list[0::2])

#difference b/w string and list limit representation e.g
#string = oder set of character and only character not anyother datatype
#list = order set of element and all data type can be stored..

var_str = "Sherazmalik"
var_list1=["S","h","e","r","a","z","m","a","l","i","k"]

print(var_str[0:4])
print(var_list1[0:4])

#Build in func in list..
a = [1,2,3,"S","h","e","r","a","z"]
b = [4,5,6,"m","a","l","i","k"]
print(a)
print(b)

#if we want to concatinate b list to a then we used extend() method which extend b to a
a.extend(b)
print(a)
#we can add element through append() and also this can be though extend() method
a.append(19)
print(a)
#we can remove item from list through pop() method and also through remove() method but in remove() item must be mention like

a.pop()
print(a)
a.remove(5)
print(a)
# we can perform sort method on list but if list contain two different data type then we cant sort item

r = [10,2,3,5,3,1,9,4,0,5,6,9,7]
print(r)
#after sorting is ascending order
r.sort()
print(r)
#and after soring in decending order
r.sort(reverse=True)

print(r)

#Note we can perform this operation at string or character or any type of data type in list
p = ["S","h","e","r","a","z","m","a","l","i","k"]
print(p)
#after reversing
p.reverse()
print(p)

#note we can add, find min value and max value in arithmatic value list like 
print(r)
print(min(r))
print(max(r))
print(sum(r))