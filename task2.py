from tkinter import N


def get_factorial_list(n):
    fact = 1
    facts = []
    for i in range(1, n+1):
        fact *= i
        facts.append(fact)
    return facts

print(get_factorial_list(N))