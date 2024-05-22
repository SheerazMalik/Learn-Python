#boolean return true or false
#boolean apply of comparision operator.
#6 comparision operator. 
# ==,!=, <,<=,>,>=,
a=5
b=3
print(f"a==b is {a==b} ")
print(f"a!=b is {a!=b}")
print(f"a<b is {a<b}")
print(f"a<=b is {a<=b}")
print(f"a>b is {a>b}")
print(f"a>=b is {a>=b}")

#Keywords operator:
#and operator when two condition are true or two comaprision operator is true then return true.
print(f"a!=b and a>b is {a!=b and a>b}")
#or keyword return true when at any one operator or condition true like

print(f"a==b or a!=b is {a==b or a!=b}")

#identity Operator ( is ),  ( is not )

y=5
z=5
print(y is z)

#identity operator for string 

p = "azka"
q = "azka"
print(p is q)

#Identity operator for list data type  ( we can not used identity operator for list )

var_list1=[1,2,3,4,5]
var_list2=[1,2,3,4,5]
print(id(var_list1))
print(id(var_list2))
print(var_list1 is var_list2)

#Membership operator (in), (in not)

var_member1 = "I am sheraz ahmed. i am from Mianwali punjab pakistan. i did my master from vu pakistan. i am python developer"
var_member2 ="Sheraz"

print(f"{var_member2} exist in var_memeber1 {var_member1 in var_member1}")

var_list3= [1,2,4,8,0]
var_input = int(input("Please Enter Your Number : "))
print(var_input in var_list3)
