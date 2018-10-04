from pathlib import Path
import unittest
import re


class LargestWord():
    # this method will return the largest word from file
    def get_largest_word(self, data):
        max_char_count = 0  # set initial word count to zero
        largest_word = None

        # do a clean up on special characters & numbers, replace them with a space
        data = re.sub('[^A-Za-z]+', ' ', data)
        for char in '!.?*;-,--@#$%&(}{][|})+~></\n':
            data = data.replace(char, ' ')


# split each word from file using space as a delimiter and iterate on the list
        for word in data.split():
            # check if each word length is greater than previous iteration if true assigning the largest word as current
            print(word)
            if max_char_count < len(word):
                max_char_count = len(word)
                largest_word = word
        return largest_word

    # transpose the largest word using python slicing

    def transpose_largest_word(self, data):
        largest_word = self.get_largest_word(data)
        return largest_word[::-1]
