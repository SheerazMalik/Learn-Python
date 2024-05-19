# Learn-Python
Learn Python for EveryOne! </br></br>

**What  is Indentation** </br></br>
Concept of spacing. Normally 4 space like tab..</br>

**Variable**</br>

#Variable is a name of memory location which store Value OR variable is storage of value OR variable is like a container which store value

""" 1. We can not Represent with numbers like    986= 123
    2. we can not used numbers at starts like..   23test = 10
    3. we can not used Special keywords  like .. $#% =10
"""

name = "Sheraz Ahmad"
age = 28
      
print(name)
print(age)
#another way of Represent variable#
a,b =20,10
print(a,b)</br></br>

**Data Types**</br>

#Numeric DataTypes 1. Int (Whole Number) 2. float(Deci numbers)#
#used for performing basic operation#

a=20 
b=10

print(a+b)
print(a-b)
print(a/b)
print(a//b)   will return whole number
print(a%b)    Jo bhe baqia aya wo mean reminder</br></br>

**Sequence of Operation**
</br>

**PEDMAS Rule**
</br>
1. Parenthesis 
2. Exponent
3. Division
4. Multiplication
5. Addition
6. Subtration
</br>

**Augumented Assignment**

An assignment operator is an operator that is used to assign some value to a variable. Like normally in Python, we write “a = 5“ to assign value 5 to variable ‘a’. Augmented assignment operators have a special role to play in Python programming. It basically combines the functioning of the arithmetic or bitwise operator with the assignment operator. So assume if we need to add 7 to a variable “a” and assign the result back to “a”, then instead of writing normally as “a = a + 7“, we can use the augmented assignment operator and write the expression as “a += 7“. Here += has combined the functionality of arithmetic addition and assignment.

So, augmented assignment operators provide a short way to perform a binary operation and assigning results back to one of the operands. The way to write an augmented operator is just to write that binary operator and assignment operator together. In Python, we have several different augmented assignment operators like +=, -=, *=, /=, //=, **=, |=, &=, >>=, <<=, %= and ^=. Let’s see their functioning with the help of some exemplar codes:</br></br>

**String**</br>
1. string is sequence of character#
2. string value will be in double quotation#
3. if Double quotation used in our sentence then we used single quotation in string representation#

name = "Sheraz Ahmad"
print(name)

#slice </br>
1. we can access one by one character through giving adress which called indexing# 
2. in pythong indexing start from 0 

print(name[0])</br>
print(name[1])</br>
print(name[2])</br>
print(name[3])</br>
print(name[4])</br>
print(name[5])</br>

#if system gothrough R to L then indexing start from -1 like </br>
print("---------------------------------------") </br>
print(name[-6])</br>
print(name[-5])</br>
print(name[-4])</br>
print(name[-3])</br>
print(name[-2])</br>
print(name[-1])</br>

**if we want to print through limit then we used like this**  </br>
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

#Note: in python T and t are two different char so this return false...</br>

**List**

1. Seq of Element
2. we can store different data type element, list of differnt data types
3. list define item reperent in sequare brackets and differentate through comma, 
var_list["a","b",[1,2,3,4],"y","z"]

#difference b/w string and list limit representation e.g </br>
#string = oder set of character and only character not anyother datatype </br>
#list = order set of element and all data type can be stored..</br>

var_str = "Sherazmalik"
var_list1=["S","h","e","r","a","z","m","a","l","i","k"]

print(var_str[0:4])
print(var_list1[0:4])

#Build in func in list..
a = [1,2,3,"S","h","e","r","a","z"]
b = [4,5,6,"m","a","l","i","k"]
print(a)
print(b)

#if we want to concatinate b list to a then we used extend() method which extend b to a
a.extend(b)
print(a)
#we can add element through append() and also this can be though extend() method
a.append(19)
print(a)
#we can remove item from list through pop() method and also through remove() method but in remove() item must be mention like

a.pop()
print(a)
a.remove(5)
print(a)
# we can perform sort method on list but if list contain two different data type then we cant sort item

r = [10,2,3,5,3,1,9,4,0,5,6,9,7]
print(r)
#after sorting is ascending order
r.sort()
print(r)
#and after soring in decending order
r.sort(reverse=True)

print(r)

#Note we can perform this operation at string or character or any type of data type in list
p = ["S","h","e","r","a","z","m","a","l","i","k"]
print(p)
#after reversing
p.reverse()
print(p)

#note we can add, find min value and max value in arithmatic value list like 
print(r)
print(min(r))
print(max(r))
print(sum(r))</br>


**Range**</br>

#we can create list smartly this is called range fun e.g

var_a = list(range(1,31))
print(var_a)

var_even = list(range(0,30,2))
print(var_even)

var_odd = list(range(1,30,2))
print(var_odd)</br>

**Range()**</br>

& we can Create any  list of our own choice by called range func </br>










