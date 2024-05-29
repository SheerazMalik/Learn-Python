import sys
#Generators

def my_gen(n:int):
    start = 0
    while start<n:
        yield start
        start +=1


gen_list = my_gen(1000)
  

print(gen_list)
  
print(f"This Generator takes {sys.getsizeof(gen_list)} Bytes")
print("X"*20)

itr_list = []

for val in gen_list:
    itr_list.append(val)

print(f"This gen_list takes {sys.getsizeof(itr_list)} Bytes")

