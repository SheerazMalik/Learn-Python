#her we used loop and if statment together.

ip = "192.168.1.2"
print(ip[0])
print(ip)
cln_num =""
print(len(ip))

for i in range(0,len(ip)):
    if ip[i] in "0123456789":
        cln_num = cln_num+ip[i]

print(int(cln_num))
print(type(cln_num))

print("x"*30)

tel_format="03261815796"
# print(tel_format)
# print(len(tel_format))

# for i in range(0,len(tel_format)):
list_a = [1,2,3,4,5,6]

for i in tel_format:
    k = int(i)
    j = k+1
    print(j)
    


