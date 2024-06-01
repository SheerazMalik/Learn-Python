#Here we Learn Non public and name mangling
#single underscore(_) without variable name or method name used for unused variable 
#single underscore(_) with name of method or variable name used for briefing this is private variable or method lik _x
#single underscore(_) after variable name or method name used for avoiding overshadow like print_
# Double Leading underscore : __var: Name mangled to avoid conflicts 
#Double leading and trailing underscore __var__ : magic method

import datetime
class Account():
    #Static method
    @staticmethod
    def current_time(self):
       time =datetime.datetime.now()
       return time
#python enforce or name magnled in balance and myself programmer enforce private variable to name
    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        print(f"Congratulation {self._name} Your Account is successfully created And Your Balance is {balance}")
        self.trans_list = [(Account.current_time(self),balance)]
        self.show_tans()
    def deposit(self, amount): 
        if amount>0:
            self.__balance+=amount
            self.show()
            self.trans_list.append((Account.current_time(self), amount))
    def withdraw(self, amount):
        if amount >0 and self.__balance>=amount:
            self.__balance-=amount
            self.show()
            self.trans_list.append((Account.current_time(self), amount))
        else:
            print(f"Poan Poan {self._name} Your Bankcurrpt")
    def show(self):  
        print(f"{self._name} Your New Balance is =  {self.__balance} Doller")

    def show_tans(self):
        for date, amount in self.trans_list:
            if amount > 0:
                trans_type = "Deposit"
            else:
                trans_type = "Withdraw"
                amount *=-1
            print(f"Amount {amount } doller,{trans_type} on {date}")

sheraz = Account("Sheraz", 100)
#if i want to add amount through hacking then this is not possible due to name mangling 
sheraz.deposit =500
sheraz.show_tans()
print(sheraz.__dict__)