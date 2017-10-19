def is_isogram(string):
    letters = []
    for letter in string:
        if letter in letters:
            return False
            break
        letters.append(letter)
    return True
