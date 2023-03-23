def is_palindrome_iterative(word):
    if not len(word):
        return False
    inverted = ''.join([*word[::-1]])
    return word == inverted
