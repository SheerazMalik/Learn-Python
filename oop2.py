
class kattle():
     #Universal attribute
    power_src = "Electricity"

    def __init__(self, make, price):
       
        self.make =make
        self.price = price
        self.on = False

    def switch(self):
        self.on =True

kenwood = kattle("X", 100)
hamilton = kattle("Y", 200)

print(kenwood)
print(kenwood.make)
print(kenwood.on)
kenwood.switch()
print(kenwood.on)
print(kenwood.power_src)

#Now concept of namespace we can not change  attribute value  of class through object of that class.
#we can change attribute value of class through class and after changing when we used new value accessible.

#Here we have power source electricity now we are changing power source

kattle.power_src= "Solar Panel"

#Now create object and acess attribute value

print(hamilton.power_src)

#Now we want change value of attribute through object of kattle
hamilton.power_src = "steam"

#for check of items in class terriority .__dict__

print(f"All items in class kattle {kattle.__dict__}")
print(f"All items in kenwood object of class kattle  {kenwood.__dict__}")
print(f"All items in hamilton object of class kattle {hamilton.__dict__}")
