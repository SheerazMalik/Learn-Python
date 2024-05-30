#Here we will discuss fun init

class map():

    def __init__(self, material):
        self.material = material
        print(f"i build {material}")

    def adder(self):
        x =2+2
        return x
    
house1 = map("X")
house2 = map("Y")
house3 = map("Z")
