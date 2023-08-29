def how_sum(n, array):
    tab = [None]*(n+1)
    tab[0] = []
    for i in range(n+1):
        if tab[i] != None:
            for a in array:
                if i+a <= n:
                    tab[i+a] = tab[i] +[a]
    return tab[n]



print(how_sum(17,[2,3]))
print(how_sum(300 , [7 , 14]))