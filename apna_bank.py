#Question is why we used Self in all places??
#Here we want to create bank where customer can create account, deposit amount, widthdrawl amount, and see balance...

#first we need customer name and some amount.
#We create customer from constructer or initilization because one time account create and constructure call
import datetime
class Account():
    #Static method
    @staticmethod
    def current_time(self):
       time =datetime.datetime.now()
       return time

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print(f"Congratulation {self.name} Your Account is successfully created And Your Balance is {balance}")
        self.trans_list = [(Account.current_time(self),balance)]
        self.show_tans()

        #if amount >0 then deposit amount in his account
    def deposit(self, amount): 
        if amount>0:
            self.balance+=amount
            self.show()
            self.trans_list.append((Account.current_time(self), amount))


        #if amount>0 then credit amount from his account, and show func also add in deposit and withdraw func becuase we not call show func in seperate 
    def withdraw(self, amount):
        if amount >0 and self.balance>=amount:
            self.balance-=amount
            self.show()
            self.trans_list.append((Account.current_time(self), amount))
        else:
            print(f"Poan Poan {self.name} Your Bankcurrpt")

        #Show his/her balance 
    def show(self):  
        print(f"{self.name} Your New Balance is =  {self.balance} Doller")

    def show_tans(self):
        for date, amount in self.trans_list:
            if amount > 0:
                trans_type = "Deposit"
            else:
                trans_type = "Withdraw"
                amount *=-1
            print(f"Amount {amount } doller,{trans_type} on {date}")    

#Question is why we used Self in all places
#Coz self is a name of that object which created from class 
#Here firstacct is in self, function used self because we dont know which object created at wat time 

firstacct = Account("Sheraz" , 100)
secacct = Account("Waqas", 1000)
thirdAcct = Account("Azka ", 2300)
firstacct.deposit(500)
firstacct.show_tans()
