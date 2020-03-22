import random
from player import Player

class Game(object):
    
    # Initial Game object
    def __init__(self):
        self.user = Player()
        self.ai = Player()

        self.predictor = Player()
        self.non_predictor = Player()

        self.ending = False

    # Validate left and right hand from the list of input whether they are in set{"O", "C"} or not
    def validate_hands(self, input_user):
        if(input_user[0].upper() in ["O", "C"] and input_user[1].upper() in ["O", "C"]):
            left = input_user[0]
            right = input_user[1]
            return left, right
        else:
            raise ValueError("\nBad input: correct input should be of the form CC3, where the first two letters indicate [O]pen or [C]losed state for each hand, followed by the prediction (0-4).\n")
    
    # Validate number of opening hands (guess) from the list of input whether they are in set{0, 1, 2, 3, 4} or not
    def validate_guess(self, guess):
        if(guess in list(range(5))):
            return int(guess)
        else:
            raise ValueError("\nBad input: prediction should be in the range of 0-4.\n")
    
    # Validate input for both hands and guess number of opening hands
    # And check whether the user is the predictor or not
    def validate_input(self, player, input_player):
        if(len(input_player) == 3):
            if(player == self.predictor):
                left, right = self.validate_hands(input_player[0:2])
                guess = self.validate_guess(int(input_player[2]))
                return left, right, guess
            else:
                raise IndexError("\nBad input: no prediction expected, you are not the predictor.\n")
        elif(len(input_player) == 2):
            if(player == self.non_predictor):
                left, right = self.validate_hands(input_player[0:2])
                return left, right
            elif(player == self.predictor):
                raise IndexError("\nBad input: you are the predictor, prediction expected\n")
            else:
                raise IndexError("\nBad input: no prediction expected, you are not the predictor.\n")
        else:
            raise IndexError("\nBad input: the length of input is more than 3\n")
        
    # Assign the predictor of this game
    def set_predictor(self, player):
        if(player == self.user):
            self.predictor = self.user
            self.non_predictor = self.ai
        else:
            self.predictor = self.ai
            self.non_predictor = self.user
    
    # Random assign the predictor of this game
    def random_predictor(self):
        self.predictor = random.choice([self.user, self.ai])
        if(self.predictor == self.user):
            self.non_predictor = self.ai
        else:
            self.non_predictor = self.user
    
    # Count the number of opening hands from both predictor and non-predictor player
    def count_open(self):
        arr = [self.predictor, self.non_predictor]
        count = 0

        for player in arr:
            if(player.left == "O"):
                count += 1
            if(player.right == "O"):
                count += 1
        return count
    
    # Evaluate the winner of this game by checking guess number with actual opening hands from predictor and non-predictor player
    def evaluate(self):
        if(self.predictor.guess == self.count_open()):
            print("You WIN!!\n")
            self.ending = True
            self.set_predictor(self.user)
        else:
            print("No winner.\n")
            self.ending = False
            self.set_predictor(self.non_predictor)
            
