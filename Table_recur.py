#Here we develop table through recursive function

def table(num,i):
    result = num * i 
    print(f"{num} x {i} = {result}")  
    i +=1
    while i!=11:
        table(num,i)
        break

table_argument1 = int(input("Please Enter your First Number which you want table :  "))

table(table_argument1,1)