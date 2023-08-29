def grid_traveler(n,m):
    tab = [[0]*(n+1) for _ in range(m+1)]
    tab[1][1] = 1
    for i in range(m+1):
        for j in range(n+1):
            if i+1<=m:
                tab[i+1][j] += tab[i][j]
            if j+1<=n:
                 tab[i][j+1] += tab[i][j]
    return tab[m][n]

print(grid_traveler(20,20))