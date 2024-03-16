"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """Class for finding random words from dictionary.

    >>> wf = WordFinder("simple.txt")
    3 words read

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    """

    def __init__(self,path):
        """Reads from dictionary and displays number of items read"""

        file = open(path)

        self.words = self.parse(file)

        print(f"{len(self.words)} words read")

    def parse(self, file):
        """Parse file to list of words."""

        return [word.strip() for word in file]

    def random(self):
        """Return a random word."""

        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """Subclass - that uses WordFinder and changes needed
        parts that excludes blank lines and comments
        
    >>> swf = SpecialWordFinder("complex.txt")
    3 words read

    >>> swf.random() in ["pear", "carrot", "kale"]
    False

    >>> swf.random() in ["kale", "apple", "mango"]
    True
    """

    def parse(self, file):
        """Parse file to list of words excluding blanks/comments."""

        return [word.strip() for word in file
                if word.strip() and not word.startswith("#")]
