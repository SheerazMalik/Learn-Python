#Here we discuss else part in list comprehension 
#we have list of char
#check in list if G exist then print skipped item if not then print sublist of List

my_list = [["A","B","C",],["D","E","F",],["G","H","I"]]

#First we learn in normal ways through loop.
my_new_list = []

for i in my_list:
    if "G" not in i:
        my_new_list.append(i)
    else:
        my_new_list.append("Letter was skipped")

print(my_new_list)
print("X"*20)

# We learn already  list comprehension have 3 parts first expression which we want 2nd for loop 3rd condition statment 
#and i we have nested if or nested for loop then 1 expression which we want 2. for loop 3. nested for loop same like 1. expression 2. for loop 3. statment 4.nested if 
#but in case of else part then scenior fully changed 1. expression then 2. if part 3. else part and at last loop
#Now through list comprehension way

my_new_list_comp = [i  if "G" not in i  else "Letter was skipped" for i in my_list ]
print(my_new_list_comp)




