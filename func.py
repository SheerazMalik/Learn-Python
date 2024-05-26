"""   Here we discuss about function. why we used function.. ans is We use functions to achieve efficiency and to perform repetitive tasks.
We have Data, if data then obviously question raise which type of data. we have differnt type of data. 
Numeric, seq, dictionary and sets, boolean, then for process these data we used control flow stament(if else) and loop
 for performing reaptitve task.   so we used function for performing these process and achiving effeciency we used these 
  process into chucks or block and every block some task perform so we create fuc for every block which perform task
 """
# 6th Element of fun 1.def, 2.Name, 3.input, 4.statment of block of code, 5. Return, 6.Return Value

def addition(x,y):
    z = x+y
    return z

a = addition(10,21)
print(a)
print("A"*50)
#ok now we discuss parameters and arguments. Parameters define in func defination while arguments gives at func calling time
#We can provide only as many arguments as the number of parameters defined in the function definition.

def subtraction(a,b,c,d):
    z =(a-b)+(c-d)
    return z


x=subtraction(10,4,13,7)
print(x)
print("B"*50)
#if we provide less argument as compared to parameter then error occur and if provide more then parameter then also 
#error occur this is called regid func. so as a programmer we want flexibility. in python *args in argument is a solution

def multiplication(*args):
    print(args[0]*args[1])
   

multiplication(5,3,10,12,45,23,54,67,99,100)
print("C"*50)
#No matter how many arguments you provide. No error will be occured.......

#now we use best approach.. but how.. *args in tuple form. so for accessing all elements of args we used for loop.

def sum_fun(*args):
    result =0
    for i in args:
        result+=i
    print(result)

sum_fun(10,7,8,6,4,3,2,1,6,8,9)

