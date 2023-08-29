def can_construct(s, array,memo={}):
    if s in memo:
        return memo[s]
    if s == "":
        return True
    for a in array:
        if s.find(a) == 0:
            if can_construct(s.replace(a,"",1) ,array) == True:
                memo[s]= True
                return memo[s]
    memo[s] = False
    return memo[s]

print(can_construct("abcdef", ["abc" , "ab" , "ef" , "ndef"]))
print(can_construct("supercalifragilisticexpialidocious", ["super", "cali", "fragil", "istic", "ex", "piali", "doc", "ious", "sup", "exp"]))
print(can_construct("abcdefghijklmno", ["ab", "cd", "ef", "gh", "ij", "kl", "mn", "op", "abc", "def", "ghi"]))
print(can_construct("abracadabra", ["abra", "cad", "abrac", "ad", "abra", "br", "aca", "dab", "ra"]))
print(can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", 
    [
    "eee", 
    "eeeee", 
    "eeeeeeee", 
    "eeeeeeeeee", 
    "eeeeeeeeeeeee", 
    "eeeeeeeeeeeeeee", 
    "eeeeeeeeeeeeeeeeeeeee",
    "eeeeeeeeeeeeeeeeeeeeee", 
    "eeeeeeeeeeeeeeeeeeeeeeeeeee"
]
))
