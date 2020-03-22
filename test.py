import unittest
from player import Player
from game import Game
import random

class PlayerTests(unittest.TestCase):

    def test_set_hands(self):
        player = Player()
        player.set_hands("o", "c")

        self.assertEqual(player.left, "O")
        self.assertEqual(player.right, "C")

    def test_random_hands(self):
        player = Player()
        player.random_hands()

        self.assertIsNotNone(player.left)
        self.assertIsNotNone(player.right)

    def test_random_shout(self):
        player = Player()
        player.random_shout()

        self.assertTrue(0 <= player.guess <= 4)
    
    def test_shout(self):
        player = Player()
        player.set_hands("O", "C")
        player.shout(3)

        self.assertEqual(player.guess, 3)
    
class GameTests(unittest.TestCase):

    def test_validate_hands(self):
        game = Game()
        game.set_predictor(game.user)
        left, right = game.validate_hands(list("oc"))

        game.predictor.set_hands(left, right)
        
        self.assertEqual(game.predictor.left, "O")
        self.assertEqual(game.predictor.right, "C")
    
    def test_validate_guess(self):
        game = Game()
        game.set_predictor(game.user)
        guess = game.validate_guess(3)

        game.predictor.shout(guess)

        self.assertEqual(game.predictor.guess, 3)

    def test_validate_input(self):
        game = Game()
        game.set_predictor(game.user)
        left, right, guess = game.validate_input(game.user, list("oo4"))

        game.predictor.set_hands(left, right)
        game.predictor.shout(guess)

        self.assertEqual(game.predictor.left, "O")
        self.assertEqual(game.predictor.right, "O")
        self.assertEqual(game.predictor.guess, 4)

    def test_set_predictor(self):
        game = Game()
        game.set_predictor(game.user)

        self.assertEqual(game.predictor, game.user)

    def test_random_predictor(self):
        game = Game()
        game.random_predictor()
        
        self.assertIsNotNone(game.predictor)
        self.assertIsNotNone(game.non_predictor)

    def test_count_open(self):
        game = Game()
        game.set_predictor(game.user)

        game.predictor.set_hands("O", "C")
        game.non_predictor.set_hands("O", "O")

        number_open = game.count_open()

        self.assertEqual(number_open, 3)

    def test_evaluate(self):
        game = Game()
        game.set_predictor(game.user)

        game.predictor.set_hands("O", "C")
        game.non_predictor.set_hands("O", "O")

        game.predictor.shout(3)
        game.evaluate()

        self.assertEqual(game.ending, True)
    
if __name__ == "__main__":
    unittest.main()