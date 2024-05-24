# while loop iterate even condition is false.

a = 1
print(id(a))

while a<10:
    print(f"{a} is less then 10")
    a +=1
    print(id(a))

print("Loop End")

#we want to skip any words from string then.....

myString = "My Name iS Sheraz Ahmad. i am from Mianwali. I am graduated from VU"
i = 0
while i <len(myString):
    if myString[i] == "S":
        i+=1
        continue
    if myString[i] ==" ":
        i+=1
        continue
    print(myString[i])
    i+=1

  