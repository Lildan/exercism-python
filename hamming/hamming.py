def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Different lengths")

    lsa = list(strand_a)
    lsb = list(strand_b)

    i = 0
    dist = 0 
    while i < len(lsa):
        if lsa[i] != lsb[i]:
            dist += 1
        i += 1
    
    return dist

