def rotate(text, key):
    lower_alphabet = list(map(chr,range(ord('a'),ord('z')+1)))
    upper_alphabet = list(map(chr,range(ord('A'),ord('Z')+1)))
    cipher = []
    for char in text:
        char_to_append = ''
        if char.isalpha():
            if char.isupper():
                char_to_append = upper_alphabet[(upper_alphabet.index(char)+key)%26]
            elif char.islower():
                char_to_append = lower_alphabet[(lower_alphabet.index(char)+key)%26]
        else:
            char_to_append = char

        cipher.append(char_to_append)
    
    return ''.join(cipher)
