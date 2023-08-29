def best_sum(n,array):
    tab = [None]*(n+1)
    tab[0] = []

    for i in range(n+1):
        if tab[i] != None:
            for a in array:
                if i+a <= n:
                    if tab[i+a] == None:
                        tab[i+a]= tab[i+a] = tab[i] +[a]
                    else:
                        if len(tab[i+a]) > len(tab[i]):
                            tab[i+a] = tab[i] +[a]
    return tab[n]

print(best_sum(8, [5,2,3]))
print(best_sum(17, [5, 3 ,4]))
print(best_sum(300 , [6 , 14]))