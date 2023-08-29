def best_construct(s, array):
    tab = [None]*(len(s)+1)
    tab[0] = []
    for i in range(len(s)+1):
        if tab[i] is not None:
            for a in array:
                if i+len(a) <= len(s) and a == s[i:i+len(a)]:
                    if tab[i+len(a)] == None:
                        tab[i+len(a)] = tab[i] + [a]
                    else:
                        if len(tab[i+len(a)]) >= len(tab[i])+1:
                            tab[i+len(a)] = tab[i] + [a]

    return tab[len(s)]

print(best_construct("abcdef", ["abc" , "ab" , "ef" , "ndef"]))
print(best_construct("supercalifragilisticexpialidocious", ["super", "cali", "fragil", "istic", "ex", "piali", "doc", "ious", "sup", "exp"]))
print(best_construct("abcdefghijklmno", ["ab", "cd", "ef", "gh", "ij", "kl", "mn", "op", "abc", "def", "ghi"]))
print(best_construct("abracadabra", ["abra", "cad", "abrac", "ad", "abra", "br", "aca", "dab", "ra"]))
print(best_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", 
    [
    "eee", 
    "eeeee", 
    "eeeeeeee", 
    "eeeeeeeeee", 
    "eeeeeeeeeeeeef", 
    "eeeeeeeeeeeeeee", 
    "eeeeeeeeeeeeeeeeeeeee",
    "eeeeeeeeeeeeeeeeeeeeee", 
    "eeeeeeeeeeeeeeeeeeeeeeeeeee"
]
))