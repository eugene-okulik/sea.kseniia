words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}


def printer(dictionary):
    for word, number in dictionary.items():
        print(word * number)


printer(words)
