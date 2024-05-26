#Here we will discuss Read file from Files input and output section
#First we discuss how many ways to read file
#in first way we open file and then close file becuase if did not do this then file can be corrupt.

aboutMe = open("Learn-Python/textfile.txt","r")

for line in aboutMe:
    if "Ahmad" in line:
            print(line)
print(type(line))
aboutMe.close()
print("A"*50)

# another way for reading data from file.. in this way we are not worry about close file becuase its create temporary file for reading data 

with open("Learn-Python/textfile.txt","r") as file:
    for line in file:
        if "Ahmad" in line:
            print(line)
    print(type(line))
    print("B"*50)
#Now we discuss method which used for reading data from file       1. Read()  
#through read() function file read by character wise...(all lines).. we can reverse all characters
with open("Learn-Python/textfile.txt","r") as file:
    line= file.read()
    print(type(line))
    print(line)
print("C"*50)

#Now we discuss 2nd method which used for reading data from file       2. Readline()  
#Through readline() function file read just one line. 
with open("Learn-Python/textfile.txt","r") as file:
    line= file.readline()
    print(type(line))
    print(line)
print("D"*50)

#Now we discuss 3rd method which used for reading data from file       3. Readlines()  
#Through this method output will be delivered in list form which is not efficient.. Reverse just lines not characters....
with open("Learn-Python/textfile.txt","r") as file:
    line= file.readlines()
    print(type(line))
    print(line)
print("E"*50)

# try:
#     with open("Learn-Python/textfile.txt", "r", encoding="utf-8") as file:
#         line = file.readline()
#         if line:
#             print(line)
#         else:
#             print("The file is empty.")
# except FileNotFoundError:
#     print("The file was not found. Please check the file path.")
# except Exception as e:
#     print(f"An error occurred: {e}")
