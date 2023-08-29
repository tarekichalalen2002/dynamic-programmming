def grid_traveler(m, n,memo={}):
    key1 = str(m)+','+str(n)
    key2 = str(n)+','+str(m)

    if key1 in memo:
        return memo[key1]
    if key2 in memo:
        return memo[key2]
    if m==1 and n==1:
        return 1
    if m * n == 0:
        return 0
    memo[key1] = grid_traveler(m-1,n,memo) + grid_traveler(m,n-1,memo)
    memo[key2] = grid_traveler(m-1,n,memo) + grid_traveler(m,n-1,memo)
    return memo[key1]

print(grid_traveler(20,20))