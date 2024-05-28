import os
list_os = os.walk("E:\\all data for programming\\practice\\GITDEMO\\Learn-Python")

for root, direct, files in list_os:
    # print(root)
    # for i in direct:
    #     print(i)
    for j in files:
        if "R" in j:
            print(j)