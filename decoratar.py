#here we discuss decorator...

def chees_and_buns(original_fun):
    def wrap():
        print("I am upper bread")
        original_fun()
        print("I am lower bread")
    return wrap

@chees_and_buns
def chicken():
    print("I am Roasted chicken")



chicken()
# buger = chees_and_buns(chicken)
