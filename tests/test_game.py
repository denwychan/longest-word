from longest_word.game import Game
import string

class TestGame:
    def test_game_initialization(self):
        # setup
        game = Game()
        # exercise
        test_grid = game.grid
        # verify
        assert type(test_grid) == list
        assert len(test_grid) == 9
        for letter in test_grid:
            assert letter in string.ascii_uppercase
        # teardown

    def test_is_valid(self):
        # setup
        game2 = Game()
        game2.grid = ['P', 'I', 'L', 'U', 'H', 'W', 'P', 'Y', 'K']
        # exercise
        assert game2.is_valid('PULP') == True
        assert game2.is_valid('WHIP') == True
        assert game2.is_valid('DANCE') == False

    def test_unknown_word_is_invalid(self):
        """A word that is not in the english directory should no be valid"""
        game3 = Game()
        game3.grid = ['P', 'I', 'L', 'U', 'H', 'W', 'P', 'Y', 'K'] # Force the grid to a test case:
        assert game3.is_valid('LKPPU') == False
        assert game3.is_valid('HULK') == True
