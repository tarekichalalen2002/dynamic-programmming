def can_construct(s ,array):
    tab = [False]*(len(s)+1)
    tab[0] = True
    for i in range(len(s)+1):
        if tab[i] == True:
            for a in array:
                if i + len(a) <= len(s) and s[i:i+len(a)] == a:
                        tab[i+len(a)] = True
    return tab[len(s)]


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
