#Here we do exercise of for and if

grocery = ["Egg","Milk","Meal","Atta","Makhan"]

for x in grocery:
    if x == "Meal":
        print(" I dont need Meal")
        continue
    print(x)

#Check prim number is or is not

num = int(input("Please Enter your number  : "))   
if num>2:
    for i in range(2,num):
        if num % i ==0:
            print(f"{num} is not prime Number")
            print(f"{i} times {num//i} is = {num}")
            break
        else:
            print(f"{num} is prime number waoooooo")
else:
    print(f"{num} is not prime number")