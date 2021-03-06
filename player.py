import random

class Player(object):

    # Inintial Player object
    def __init__(self):
        self.left = ""
        self.right = ""
        self.guess = -1
    
    # Set left and right hand of player
    def set_hands(self, left, right):
        self.left = left.upper()
        self.right = right.upper()

    # Generate randomly left and right hand of player
    def random_hands(self):
        hand = ['O', 'C']
        self.left = random.choice(hand)
        self.right = random.choice(hand)

    # Random guess the number of opening hands
    def random_shout(self):
        possible_guess = [0, 1, 2, 3, 4]
        self.guess = random.choice(possible_guess)

    # Guess the number of opening hands directly
    def shout(self, number):
        self.guess = number
    

