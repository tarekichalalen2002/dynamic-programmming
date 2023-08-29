def how_sum(n , array, memo={}):
    if n in memo:
        return memo[n]
    if n == 0 :
        return []
    
    if n<0:
        return None

    for a in array:
        result = how_sum(n-a,array, memo)
        if result is not None:
            memo[n] = result + [a] 
            return memo[n]
    memo[n] = None
    return memo[n]

print(how_sum(300,[14,6]))