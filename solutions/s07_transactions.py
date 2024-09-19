class Account:
    def __init__(self, id):
        self.id = id
        self.balance = 0
        self.num_transactions = 0
        self.transactions = []

    def update(self, money):
        if self.balance + money < 0:
            print("Insufficient funds")
        else:
            self.balance = self.balance + money
            self.num_transactions += 1
            self.transactions.append((self.num_transactions, money))

    def print_balance(self):
        print("Balance:", self.balance)

    def print_transactions(self):
        print("--- Transactions ---")
        for tid, money in self.transactions[-5:]:
            print(f"tid {tid}: {money}")
        self.print_balance()


jhon = Account(id=0)
for i in range(1, 10):
    jhon.update(i * 10)
jhon.print_transactions()
