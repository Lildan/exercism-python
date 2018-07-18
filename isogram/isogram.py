def is_isogram(string):
    ls = list(string.lower())
    ls.sort()
    print(ls)
    i = 0
    while i < len(ls) - 2:
        if ls[i] == ls[i+1] and ls[i].isalpha():
            return False
        i+=1
    return True

