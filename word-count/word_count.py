def word_count(phrase):
    ls = phrase.lower().split()
    dict = {}
    for word in ls:
        if  word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    
    return dict