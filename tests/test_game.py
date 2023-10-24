from longest_word.game import Game
import string

class TestGame:
    def test_game_initialization(self):

        my_game= Game()
        grid= my_game.grid

        assert type(grid) == list
        assert len(grid) == 9

        for each in grid:
            assert each in string.ascii_uppercase



    def empty_word_test(self):

        my_game=  Game()

        assert my_game.is_valid('') is False

    def valid_test(self):

        my_game= Game()
        test_grid= 'OQUWRBAZE'
        test_word= 'BAROQUE'
        my_game.grid= list(test_grid)

        assert my_game.is_valid(test_word) is True
        assert my_game.grid== list(test_grid)


    def invalid_test(self):

        my_game= Game()
        test_grid= 'OQUWRBAZE'
        test_word= 'BLAZE'
        my_game.grid= list(test_grid)

        assert my_game.is_valid(test_word) is False
        assert my_game.grid == list(test_grid)
