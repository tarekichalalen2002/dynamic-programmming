def can_sum(n , array , memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return True
    if n < 0:
        return False
    for a in array:
        remainder = n-a
        if(can_sum(remainder,array,memo) == True):
            memo[n] = True
            return memo[n]

    memo[n] = False
    return memo[n]

print(can_sum(300 , [14,7]))