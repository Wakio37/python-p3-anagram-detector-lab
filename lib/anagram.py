# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        matches = []
        sorted_word = sorted(self.word)
        
        for potential_anagram in word_list:
            if potential_anagram != self.word and sorted(potential_anagram) == sorted_word:
                matches.append(potential_anagram)
        
        return matches
