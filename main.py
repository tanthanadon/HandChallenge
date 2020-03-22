from player import Player
from game import Game

def main():
    game = Game()
    # The predictor of the first round is USER player
    game.set_predictor(game.user)

    continue_flag = True
    print("\nWelcome to the game!\n")
    # The game will start and end when the game has the winner
    # After the game has the wiiner, it will ask user whether they want to play again or not
    while(continue_flag):
        # At the end of game.evalaute(), it will swap the predictor from USER to AI player
        # And do it again when the game does not have the winner
        if(game.ending == False):
            # If there are raised exceptions from any functions
            # they will be catched, print the error, and continue the loop again
            try:
                if(game.predictor == game.user):
                
                    input_player = list(input("You are the predictor, what is your input?\n\n"))
                    left, right, guess = game.validate_input(game.predictor, input_player)
                    game.predictor.set_hands(left, right)
                    game.predictor.shout(guess)
                    game.non_predictor.set_hands("O", "C")
                    print("\nAI: {0}{1}\n".format(game.non_predictor.left, game.non_predictor.right))
                    game.evaluate()

                else:
                    game.predictor.random_hands()
                    game.predictor.random_shout()
                    print("AI is the predictor, what is your input?\n")
                    input_player = list(input(""))
                    game.validate_input(game.non_predictor, list(input_player))
                    game.non_predictor.set_hands(left, right)

                    print("\nAI: {0}{1}{2}\n".format(game.predictor.left, game.predictor.right, game.predictor.guess))
                    game.evaluate()

            except ValueError as v:
                print("{}".format(v))
                print("Please try again!\n")
                continue
            except TypeError:
                print("Input must be a list.\n")
                print("Please try again!\n")
                continue
            except IndexError as i:
                print("{}".format(i))
                print("Please try again!\n")
                continue
        else:
            con = input("\nDo you want to play again?\n")
            if(con.upper() == "Y"):
                continue_flag = True
                game.ending = False
            elif(con.upper() == "N"):
                continue_flag = False
                print("Ok, bye!")
            print("")

if __name__ == '__main__':
    main()