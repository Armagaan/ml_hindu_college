class Account:
    def __init__(self, id):
        self.id = id
        self.balance = 0

    def update(self, money):
        if self.balance + money < 0:
            print("Insufficient funds")
        else:
            self.balance = self.balance + money

    def print_balance(self):
        print("Balance:", self.balance)


jhon = Account(id=0)
jhon.print_balance() # View balance

jhon.update(100) # Credit money
jhon.print_balance() # View balance

jhon.update(-150) # Handle insufficient balance. The program should not crash here. Display a msg.
jhon.print_balance() # View balance

jhon.update(-50) # Debit money
jhon.print_balance() # View balance
