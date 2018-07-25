def hey(phrase):
    phrase = phrase.strip()

    if phrase.endswith('?') and phrase.isupper():
        return "Calm down, I know what I'm doing!"
    elif phrase.endswith('?'):
        return 'Sure.'
    elif phrase.isupper() or  (phrase.isupper() and not phrase.endswith('?')):
        return 'Whoa, chill out!'
    elif phrase == "":
        return 'Fine. Be that way!'

    return 'Whatever.'

