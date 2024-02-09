class Account:
    def __init__(self, balance):
        self.bal = balance
    
    def withd(self, withd):
        self.withd = withd
        if self.bal - self.withd < 0:
            print("You have no money beasch")
        else:
            print("get ut money greedy mf")
            self.bal -= self.withd
    
    def deposit(self, dep):
        self.dep = dep
        print("aight mf now i got ya money")
        self.bal += dep

account = {}

def create_acc(owner, in_bal):
    account[owner] = Account(in_bal)

def deposit(owner, amount):
    if owner in account:
        account[owner].deposit(amount)
    else:
        print("you aint in that list")

def withdrawal(owner, amount):
    if owner in account:
        account[owner].withd(amount) 
    else:
        print("you aint in that list")

create_acc("Ali", 1000)
create_acc("Dulat", 500)

deposit("Ali", 200)
withdrawal("Arlan", 100)
withdrawal("Dulat", 1500)
