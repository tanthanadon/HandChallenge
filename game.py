import random
from player import Player

class Game(object):
    
    def __init__(self):
        self.user = Player()
        self.ai = Player()

        self.predictor = Player()
        self.non_predictor = Player()

        self.ending = False
    
    def set_predictor(self, player):
        if(player == self.user):
            self.predictor = self.user
            self.non_predictor = self.ai
        else:
            self.predictor = self.ai
            self.non_predictor = self.user

    def random_predictor(self):
        self.predictor = random.choice([self.user, self.ai])
        if(self.predictor == self.user):
            self.non_predictor = self.ai
        else:
            self.non_predictor = self.user
    
    def count_open(self):
        arr = [self.predictor, self.non_predictor]
        count = 0

        for player in arr:
            if(player.left == "O"):
                count += 1
            if(player.right == "O"):
                count += 1
        
        return count
        
    def validate(self):
        if(self.predictor.guess == self.count_open()):
            print("You WIN!!")
            self.ending = True
            self.set_predictor(self.user)
        else:
            print("No winner.")
            self.ending = False
            self.set_predictor(self.non_predictor)
            
