def all_construct(s,array , memo={}):
    if s in memo:
        return memo[s]
    if s == "" :
        return [[]]
    
    result = []
    for a in array:
        if s.find(a) == 0 :
            suffix = s.replace(a,"" ,1)
            suffix_ways = all_construct(suffix,array,memo)
            target_ways = list(map(lambda x: [a]+x ,suffix_ways)) 
            result += target_ways

    memo[s] = result
    return result

print(all_construct("abcdef", ["abc" , "ab" , "ef" , "def"]))
print(all_construct("purple", ["purp" , "p" , "ur" , "le" , "purpl"]))
print(all_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", 
    [
    "ee", 
    "eee", 
    "eeeee", 
    "eeeeeeef", 
    "eeeeeeeee",
    "eeeeeeeeeee",
    "eeeeeeeeeeeeeee",
    "eeeeeeeeeeeeeeeeee", 
]
))