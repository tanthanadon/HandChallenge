import random

class Player(object):

    def __init__(self):
        self.left = ""
        self.right = ""
        self.guess = -1
    
    def set_hands(self, left, right):
        self.left = left.upper()
        self.right = right.upper()

    def random_hands(self):
        hand = ['O', 'C']
        self.left = random.choice(hand)
        self.right = random.choice(hand)

    def random_shout(self):
        possible_guess = [0, 1, 2, 3, 4]
        self.guess = random.choice(possible_guess)

    def shout(self, number):
        self.guess = number
    

