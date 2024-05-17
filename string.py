#string is sequence of character#
#string value will be in double quotation#
#if Double quotation used in our sentence then we used single quotation in string representation#

name = "Sheraz"
print(name)

#slice
#we can access one by one character through giving adress which called indexing# 
#in pythong indexing start from 0 to onward from L TO R (left to right)


print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])

#if system gothrough R to L then indexing start from -1 like
print("---------------------------------------")
print(name[-6])
print(name[-5])
print(name[-4])
print(name[-3])
print(name[-2])
print(name[-1])
print("++++++++++++++++++++++++++++++++")



#if we want to print through limit then we used like this
quote = "SherazAhmad and Waqas Ahmad"
print(quote)
 
print(quote[0:10])

#if we want to skip any character in string then we used stepsize e.g

print(quote[0:10:2])

#first start point then End point and then step size mean itne ko choor ko itne wala print hona hai 
#if we dont know about end point then we put :: (double colon)
print(quote[0::])

#Note:  Even empty space is treated as a character
#2 types of arithmatic operation can be performed on string 
# when we add two string then we called concatination like

firstName = "Sheraz"
secondName = "Malik"
print(firstName+" "+secondName)

#we can multiply string also..
print(firstName*3)

#String Formating
#two ways or type of string formating.
# 1. New type

stdName= "Sarmad"
age=13
message= f"Hello my name is {stdName}, and i am {age} Years old. I am Learning Python"
print(message)
#2nd way is old so dont discuss....


#taking input from users and then giving output 

clientName = input("Please Enter Your Name  ")
age = int(input("Please Enter Your Age  "))

print(f"My Client Name is {clientName}, and his age is {age}")

#we used int exclude data type because input function treat all input data in string form so when age is taken then convert to int
#we can perform any task on age coz this is int value

#Build in function for string or string build in function in python e.g
statment = "This is python Course, i am learning and practicing Python and pushing all data on GitHub"

#First function is lower() which change all character to lower case e.g

print(statment.lower())

# 2. Upper() is build in string function which convert all character to upper case e.g

print(statment.upper())

#3. strip() is buildin str function which remove unnecassary white spaces.

print(statment.strip())

# 4. split() is build in func which split string and return output in list form. e.g

print(statment.split())

#. 5 fint() is build in func which find character indexing or location

print(statment.find("and"))

#6. replace() is a build in str func which find and replace char with new given char

print(statment.replace("and","OR"))

#7.  startwith() and startend() are two  build in func which find is that string start or end  with this char or not if not then return False otherwise return True.
 
print(statment.startswith("T"))
print(statment.endswith("G"))
print(statment.startswith("t"))

#Note: in python T and t are two different char so this return false...











