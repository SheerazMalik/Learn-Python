#in list we can replace any element through indexing of this element like...
var_list = [1,5,9,4,"Sarmad","Ahmad"]
print(var_list)
#Now we want to replace sarmad from Sheraz then ...
var_list[4]= "Sheraz"
print(var_list)
#this concept is called mutable. List is mutable. 

#Tuple  if element can not be changed or replace from indexing this is called imputable data type. e.g Tuple

#tuple can be defined two ways...
# 1. 
var_tuple1=1,2,3,4,5,6
print(var_tuple1)
# 2.
var_tuple2 = (1,2,3,4,5,6)
print(var_tuple2)
#if we want to change or replace element then this throw error.

"""var_tuple2[0]=0
print(var_tuple2)"""

#we can not change or replace element but we can assign new value to any tuple like...

var_tuple2 =var_tuple1[1],"S","H",var_tuple2[5]

print(var_tuple2)

#unpacking tuple

ele_a, element_b, element_c, ele_d = var_tuple2
#Note variable will be equal to tuple element coz each element assign to one variable .. var_tuple2 have 4 element so variable are also 4..

print(ele_a)
