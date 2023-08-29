def count_construct(s , array, memo = {}):
    if s in memo:
        return memo[s]
    if s == "":
        return 1
    total_count = 0
    for a in array:
        if s.find(a) == 0:
            total_count += count_construct(s.replace(a,"",1) , array,memo)

    memo[s] = total_count
    return total_count


print(count_construct("abcdef", ["abc" , "ab" , "ef" , "def"]))
print(count_construct("purple", ["purp" , "p" , "ur" , "le" , "purpl"]))
print(count_construct("supercalifragilisticexpialidocious", ["super", "cali", "fragil", "istic", "ex", "piali", "doc", "ious", "sup", "exp"]))
print(count_construct("abcdefghijklmno", ["ab", "cd", "ef", "gh", "ij", "kl", "mn", "op", "abc", "def", "ghi"]))
print(count_construct("abracadabra", ["abra", "cad", "abrac", "ad", "abra", "br", "aca", "dab", "ra"]))

print(count_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", 
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