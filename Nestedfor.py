#Nested for loop. a loop which inside another for loop.
#Create talbe from 1 to 5

for i in range (1,6):
    print(f"-----------------------------")
    print(f"Table of {i}")
    for j in range (1,6):
        
        print(f"{i} * {j} =  {j*i} ")
