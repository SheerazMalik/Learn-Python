numbers = [1,2,3,4,5,12]

sum=0

for i in numbers:
    sum = sum + i
print(sum)

for j in range(21,31):
    print(j)
else:
    print("List is finished")


fruits = ("Apple", "Bnana", "Cherry")
adj = ["Red","Big","Tasty"]

     
for x,y in zip(fruits,adj):
    print(x,y)
 

#for loop on Dictionary

dic_a = {"f_name":"Sheraz", "L_name":"Ahmad","age":28, "Married":"No"} 
print(type(dic_a))
print(dic_a.items())
print(dic_a.keys())
print(dic_a.values())
for key,value in dic_a.items():
    print(key,value)
print(type(value))
print("---------------------------------------------------")

tup_a = [("A","B"),("C","D")]
for i,j in tup_a:
    print(i,j)