def reverse(input=''):
    result = ''
    inputArray = list(input)
    inputArray.reverse()
    for char in inputArray:
        result += char
    return result
        
