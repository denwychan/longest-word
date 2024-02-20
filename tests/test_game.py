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
        # Turns out you don't need to check if the word is a valid Engish word
        ## therefore removed valid word check
        assert game2.is_valid('LKPPU') == False
