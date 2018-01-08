# put your code here.
def count_words(file_name):
    """Given a file, outputs a frequency count for each count (dictionary)."""


    file = open(file_name)
    word_count = {}

    for line in file:
        tokens = line.rstrip().split(' ')

        for token in tokens:
            add_word(word_count, token)


def add_word(word_count, word):
    """Given a dictionary and word, increments the word count in the dictionary."""
