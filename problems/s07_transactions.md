Update your class `Account` so that it maintains a log of updates. Write a method that prints the ministatement. The ministatement contains the transaction ID and money credited/debited at the time for the 5 latest transactions. The ministatement should also print the balance.

Example:
```python
jhon = Account(id=0)
for i in range(1, 10):
    jhon.update(i * 10)
jhon.print_transactions()
```

Output:
```
--- Transactions ---
tid 5: 50
tid 6: 60
tid 7: 70
tid 8: 80
tid 9: 90
Balance: 450
```
