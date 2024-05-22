#Two types of coversion 1. Implicit conversion 2. explicit conversion
#Implicit conversion automatic through system 
a = 2
b = 3.14
print(a+b)
print(type(a))
print(type(b))
#Here system automatic change data type of a coz b is supperior b is floating data type so system change and sum up both

#explicit conversion or type casting

c = input ("Please enter number  :")
print(type(c))
c = int(c)
d = 10
print(c+d)
print(type(c))