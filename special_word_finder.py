from wordfinder import WordFinder


class SpecialWordFinder(WordFinder):
    """Word finder that eliminates blank lines and comments

    >>> swf = SpecialWordFinder("words_with_comments.txt")
    6 words read

    >>> swf.random() in ['cat', 'dog', 'sunshine', 'weather', '', '# comment']
    True

    >>> swf.random() in ['cat', 'dog', 'sunshine', 'weather', '', '# comment']
    True
    """

    def __init__(self, filepath):
        """Make a random word generator without comments and spaces"""
        super().__init__(filepath)

    def filter_list(self):
        """Remove blank lines and comments from the word list"""
        self.word_list = [
            word for word in self.word_list if word != '' and word[0] != '#']
