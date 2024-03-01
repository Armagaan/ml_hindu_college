Write a class named `Account` for a bank account. It should support the following methods:

```python
jhon = Account(id=0)
jhon.print_balance() # View balance

jhon.update(100) # Credit money
jhon.print_balance() # View balance

jhon.update(-150) # Handle insufficient balance. The program should not crash here. Display a msg.
jhon.print_balance() # View balance

jhon.update(-50) # Debit money
jhon.print_balance() # View balance
```

The output should look like this:
```python
Balance: 0
Balance: 100
Insufficient balance
Balance: 100
Balance: 50
```
