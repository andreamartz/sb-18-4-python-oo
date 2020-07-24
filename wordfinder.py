"""Word Finder: finds random words from a dictionary."""

from random import choice


class WordFinder:
    """Finds random words from a list

    >>> wf = WordFinder("words_short.txt")
    4 words read

    >>> wf.random() in ['cat', 'dog', 'sunshine', 'weather']
    True

    >>> wf.random() in ['cat', 'dog', 'sunshine', 'weather']
    True

    >>> wf.random() in ['cat', 'dog', 'sunshine', 'weather']
    True

    """

    def __init__(self, filepath="words.txt"):
        """Make a new random word generator"""
        self.filepath = filepath
        self.word_list = self.read_file()
        print(f"{len(self.word_list)} words read")

    def read_file(self):
        """Read a file containing words and save the words to a list"""
        # file = open(self.filepath, "r")
        # self.word_list = []
        # for line in file:
        #     line = line[:(len(line) - 2)]
        #     self.word_list.append(line)

        file = open(self.filepath, "r")
        self.word_list = file.read().splitlines()
        file.close()

        # for word in self.word_list:
        #     if word == '' or word[0] == '#':

        return [word.strip() for word in self.word_list]

    def random(self):
        """Choose and return a new random word"""
        word = choice(self.word_list)
        return word
