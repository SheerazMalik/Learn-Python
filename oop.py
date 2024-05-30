#here we discuss OOP concept class 
#class is blue print class contain attributes and methods.

class map():
    material= "House"
    print(f"i build {material}")
    def adder(self):
        x =2+2
        return(x)
    
#creating object of map class
House = map()
print(House.adder())
House.name = "X"
print(House.name)