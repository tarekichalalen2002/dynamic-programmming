def best_sum(n , array , memo={}) :
    if n in memo:
        return memo[n]
    if n == 0 :
        return []
    if n < 0 :
        return None
    shortestResult = None
    for a in array:
        remainder = n - a
        result = best_sum(remainder , array, memo)
        if result != None:
            newResult = result + [a]
            if shortestResult == None or len(newResult)<len(shortestResult):
                shortestResult = newResult

    memo[n] = shortestResult
    return memo[n]

print(best_sum(100 , [5,2,1]))