def count_construct(s , array) :
    tab = [0]*(len(s)+1)
    tab[0] = 1

    for i in range(len(s)+1):
        if tab[i] > 0:
            for a in array:
                if i+len(a) <= len(s) and s[i:i+len(a)] == a:
                    tab[i+len(a)] += tab[i]
    return tab[len(s)]


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