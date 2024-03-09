# Bank
Write a class for a bank having the following methods.

```python
bank = Bank()

# Open accounts
bank.open_account(id = 0)
bank.open_account(id = 1)

# Add balance.
s1 = bank.update(id = 0, amount = 100)
s2 = bank.update(id = 1, amount = 10)

s3 = bank.update(id = 0, amount = -200)
s4 = bank.update(id = 0, amount = -20)

print("Output 1")
print(s1, s2, s3, s4)

# Transact
s5 = bank.transaction(sender_id=0, receiver_id=1, amount=50)
print("\nOutput 2")
print(s5)

# Ministatement
print("\nOutput 3")
bank.print_statement(0)
bank.print_statement(1)
```

Here's the output:
```
Output 1
True True False True

Output 2
True

Output 3
>>> Statement: id #0
id #0: 100
id #0: -20
id #1: -50

>>> Statement: id #1
id #1: 10
id #0: 50
```
