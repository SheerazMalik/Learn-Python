#Here we discuss Nested for and if in list comprehension...

#task.  Multiply two list and value or item of list store in 3rd list 
#ok now first we do this task into normal ways.
import sys
my_list =[]

A = [1,3,5,7,9]
B = [2,4,6,8,10]

for x in A:
    for y in B:
        my_list.append(x*y)

print(my_list)


# now in list comprehension way...

my_list1 = [x*y for x in A for y in B]
print(my_list1)
