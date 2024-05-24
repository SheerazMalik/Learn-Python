#if else flow control statment 
#make checker for passed or failed 
# marks = int(input("Please Enter Your Marks"))
# passing_marks = 50
# if marks>=passing_marks:
#     print("Passed")
# else:
#     print("Failed")

#if 3 statment or condition then we used

ageStage = int(input("Please Enter Your Age  : "))

if ageStage >3 and ageStage<7:
    print("Early Childhood")
elif ageStage >6 and ageStage<12:
    print("Middle Childhood")
elif ageStage >12 and ageStage<18:
    print("Adolescence")
elif ageStage >18 and ageStage<40:
    print("Early Adulthood")
elif ageStage >40 and ageStage<65:
    print("Middle Adulthood")
else:
    print("Late Adulthood")



#  Apply Keywords Operator We have two keywords operator 1. Logical Operator and Membership Operator

#firstrly Check Logical Operator.

num = int(input("Please Enter Your Number"))

if num>5 and num<10:
    print(f"Your Number exist in b/w  5 to 10. Your Number is {num}")
else:
    print("Your are in else part")

#apply membership operator
num1=(1,2,3,4,5,6,7,8,9,10,11)
if num in num1:
    print(f"Your Number exist in b/w  5 to 10. Your Number is {num}")
else:
    print("Your are in else part")
