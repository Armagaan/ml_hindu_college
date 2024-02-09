"""Fibonacci sequence using a list as an argument."""
def cal_fib_seq_1(n, l=[0, 1]):
    # Corner cases
    if n <= 0:
        return []
    elif n < 2:
        return l[:n]

    # Recursion
    if len(l) == n:
        return l
    return cal_fib_seq_1(n, l + [l[-1] + l[-2]])

"""Fibonacci sequence without passing a list as an argument."""
def cal_fib_seq_2(n):
    def get_ith_fib_num(i):
        if i <= 1:
            return i
        return get_ith_fib_num(i-1) + get_ith_fib_num(i-2)

    seq = []
    for i in range(n):
        seq.append(get_ith_fib_num(i))
    return seq


print(">>> Using list as an argument.")
print(cal_fib_seq_1(n=-1))
print(cal_fib_seq_1(n=0))
print(cal_fib_seq_1(n=1))
print(cal_fib_seq_1(n=5))
print(cal_fib_seq_1(n=10))

print("-" * 50)

print(">>> Without list")
print(cal_fib_seq_2(n=-1))
print(cal_fib_seq_2(n=0))
print(cal_fib_seq_2(n=1))
print(cal_fib_seq_2(n=5))
print(cal_fib_seq_2(n=10))
