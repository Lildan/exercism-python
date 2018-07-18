def verify(isbn):
    ls = list(isbn)
    if len(ls) < 10:
        return False
    i = 10
    j = 0
    sum = 0
    print(ls)
    while i > 0:
        if j > len(ls) - 1:
            return False

        if ls[j] == '-':
            pass
        elif ls[j] == 'X' and i == 1:
            sum += 10
            i -= 1
        elif ls[j].isdecimal():
            sum += int(ls[j]) * i
            i -= 1
        else:
            return False
        
        j += 1
        
        if i == 0 and len(ls) > j:
            return False 

    return sum % 11 == 0
    
