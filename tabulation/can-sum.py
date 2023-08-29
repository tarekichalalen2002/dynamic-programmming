def can_sum(n , array):
    tab = [False]*(n+1)
    tab[0] = True
    for i in range(n+1):
        if tab[i] == True:
            for a in array:
                if i+a <= n:
                    tab[i+a] = True
    return tab[n]


print(can_sum(5 , [4,3]))
print(can_sum(300 , [14,6]))