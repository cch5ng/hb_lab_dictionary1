from sys import argv


def count_words(file_name):
    """Given a file, outputs a frequency count for each count (dictionary)."""

    file = open(file_name)
    word_count = {}

    for line in file:
        tokens = line.rstrip().split()

        for token in tokens:
            add_word(word_count, token.lower())

    for key, value in word_count.iteritems():
        print key, value


def add_word(word_count, word):
    """Given a dictionary and word, increments the word count in the dictionary."""

    clean_word = remove_punctuation(word)
    word_count[clean_word] = word_count.get(clean_word, 0) + 1


def remove_punctuation(word):
    """Given a word, remove punctuation if it exists (expect at end)."""

    punctuation = set([".", ",", ";", "!", "?", ":", "\"", "_", "*", "#"])
    while len(word) > 0 and word[-1] in punctuation:
        word = word[:-1]

    while len(word) > 0 and word[0] in punctuation:
        word = word[1:]

    return word

count_words(argv[1])
