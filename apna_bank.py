#Question is why we used Self in all places??
#Here we want to create bank where customer can create account, deposit amount, widthdrawl amount, and see balance...

#first we need customer name and some amount.
#We create customer from constructer or initilization because one time account create and constructure call
class Account():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print(f"Congratulation {self.name} Your Account is successfully created")


        #if amount >0 then deposit amount in his account
    def deposit(self, amount): 
        if amount>0:
            self.balance+=amount


        #if amount>0 then credit amount from his account
    def withdraw(self, amount):
        if amount >0:
            self.balance-=amount

        #Show his/her balance 
    def show(self):  
        print(f"{self.name} Your Balance is =  {self.balance} R.S")

#Question is why we used Self in all places
#Coz self is a name of that object which created from class 
#Here firstacct is in self, function used self because we dont know which object created at wat time 

firtacct = Account("Sheraz" , 100)
secacct = Account("Waqas", 1000)
firtacct.show()


thirdAcct = Account("Azka ", 10000000)
thirdAcct.deposit(280) 
thirdAcct.show()