Update your class `Account` so that it maintains a log of updates. Write a method that prints the ministatement. The ministatement contains the transaction ID and money credited/debited at the time for the 5 latest transactions. The ministatement should also print the balance.

Example:
```python
jhon = Account(id=0)
for i in range(1, 10):
    jhon.update(i)
jhon.print_transactions()
```

Output:
```
----- Ministatement -----
tid 6 | 1
tid 7 | 1
tid 8 | 1
tid 9 | 1
tid 10 | 1
Balance: 55
```
