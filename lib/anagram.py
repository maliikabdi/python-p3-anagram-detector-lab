# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()  # Convert to lowercase for case-insensitivity

    def match(self, word_list):
        # Sort the letters of the original word
        sorted_word = sorted(self.word)
        # Find all words in the list that are anagrams
        return [w for w in word_list if sorted(w.lower()) == sorted_word]

