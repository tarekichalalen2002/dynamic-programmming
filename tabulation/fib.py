def fib(n):
    tab= [0]*(n+1)
    tab[1] = 1
    for i in range(n+1):
        if i+1 <= n:
            tab[i+1] += tab[i]
        if i+2 <= n:
            tab[i+2] += tab[i]

    return tab[n]
    

print(fib(7))
print(fib(50))