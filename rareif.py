#Rare if condition.

#when we put -int or +int any number then true statment execute. at 0 false statment execute. like
if 1:
    print("You are at if part")
else:
    print("You are at else part")

#at 0
if 0:
    print("You are at if part")
else:
    print("You are at else part")
if -123:
    print("You are at if part")
else:
    print("You are at else part")  

#at list 
lis_a = [1,2,3,4,4]     
if lis_a:
    print("You are at if part")
else:
    print("You are at else part")

#when list empty
list_b = []    
if list_b:
    print("You are at if part")
else:
    print("You are at else part")