#here we continue  previous discussion....

#Global Space

def washingmachine():
    #Enclosing func

    clothes ="Dirty and Clean"
    def dryclean():
        #nested func
        nonlocal clothes
        clothes = "Dry and Clean"
        print(clothes)

    dryclean()
    print(clothes)

washingmachine()

#Variable accesing precdence in python. (LEGB) First python code find variable in local space then move to enclosing function or space
# then move to global space then move to build in function...
