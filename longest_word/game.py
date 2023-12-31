import string
import random
import requests

class Game:
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = []

        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))


    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        if not word:
            return False
        game_grid= self.grid.copy()
        for letter in game_grid:
            if letter in game_grid:
                idx= game_grid.index(letter)
                game_grid.pop(idx)
            else:
                return False
        return self.check_word(word)

    @staticmethod
    def check_word(word):
        dict_url= f"https://wagon-dictionary.herokuapp.com/{word}"
        result= requests.get(dict_url).json()
        return result['found']
