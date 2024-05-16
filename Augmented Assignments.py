
""" **Augumented Assignment**

An assignment operator is an operator that is used to assign some value to a variable. Like normally in Python, we write “a = 5“ to assign value 5 to variable ‘a’. Augmented assignment operators have a special role to play in Python programming. It basically combines the functioning of the arithmetic or bitwise operator with the assignment operator. So assume if we need to add 7 to a variable “a” and assign the result back to “a”, then instead of writing normally as “a = a + 7“, we can use the augmented assignment operator and write the expression as “a += 7“. Here += has combined the functionality of arithmetic addition and assignment.

So, augmented assignment operators provide a short way to perform a binary operation and assigning results back to one of the operands. The way to write an augmented operator is just to write that binary operator and assignment operator together. In Python, we have several different augmented assignment operators like +=, -=, *=, /=, //=, **=, |=, &=, >>=, <<=, %= and ^=. Let’s see their functioning with the help of some exemplar codes:
""" 
a=10
print(a)
a+=2
print(a)
b=10
b-=2
print(b)
c=10
c/=2
print(c)
d=10
d //=2
print(d)
e=10
e**=2
print(e)
