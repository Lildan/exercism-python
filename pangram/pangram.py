def is_pangram(sentence):
    alphabet = list(map(chr,range(ord('a'),ord('z')+1)))
    print(alphabet)
    ls = list(sentence.lower())
    ls.sort()
    filteredls = [char for char in ls if char.isalpha()]
    print(filteredls)
    i = 0
    for char in filteredls:
        if char == alphabet[i]:
            continue
        elif char == alphabet[i+1]:
            i+=1
            continue
        return False
    if alphabet[i] == 'z':
        return True
    return False





