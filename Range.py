#we can create list smartly this is called range fun e.g

var_a = list(range(1,31))
print(var_a)

var_even = list(range(0,30,2))
print(var_even)

var_odd = list(range(1,30,2))
print(var_odd)

#Exercise for Range()

list_seven = list(range(7,100,7))
print(list_seven)

input_number =int(input("Please Enter your Number:   "))

result = f"{input_number} is Divisible by seven : {input_number in list_seven}"
print(result)