
#Here we discuss list comprehension with conditional statment....
#give me  0 to 10 list ...

my_list = [x for x in range(10)]
print(my_list) 

#Ok, now  give me even number list

even = [x for x in range(10) if x%2 ==0]
print(even) 

#ok, now give me power two of this even number list 

even = [x**2 for x in range(10) if x%2 ==0]
print(even) 