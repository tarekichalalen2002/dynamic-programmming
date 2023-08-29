def how_construct(s, array):
    tab = [None]*(len(s)+1)
    tab[0] = []
    for i in range(len(s)+1):
        if tab[i] is not None:
            for a in array:
                if i+len(a) <= len(s) and a == s[i:i+len(a)]:
                    tab[i+len(a)] = tab[i] + [a]

    return tab[len(s)]

print(how_construct("abcdef", ["abc" , "ab" , "ef" , "ndef"]))
print(how_construct("supercalifragilisticexpialidocious", ["super", "cali", "fragil", "istic", "ex", "piali", "doc", "ious", "sup", "exp"]))
print(how_construct("abcdefghijklmno", ["ab", "cd", "ef", "gh", "ij", "kl", "mn", "op", "abc", "def", "ghi"]))
print(how_construct("abracadabra", ["abra", "cad", "abrac", "ad", "abra", "br", "aca", "dab", "ra"]))
print(how_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", 
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