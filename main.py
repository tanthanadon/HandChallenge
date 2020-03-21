from player import Player
from game import Game

def get_input():
    string = input()
    input_user = list(string)
    if(len(input_user) == 3):
        left = input_user[0]
        right = input_user[1]
        guess = int(input_user[2])
        return left, right, guess
    elif(len(input_user) == 2):
        left = input_user[0]
        right = input_user[1]
        return left, right
    else:
        print("Error")
        return []

def main():
    game = Game()
    game.set_predictor(game.user)

    continue_flag = True
    print("\nWelcome to the game!\n")
    # game.ending = True
    while(continue_flag):
        if(game.ending == False):
            if(game.predictor == game.user):
                print("You are the predictor, what is your input?\n")
                left, right, guess = get_input()

                game.predictor.set_hands(left, right)
                game.predictor.shout(guess)

                game.non_predictor.random_hands()
                print("\nAI: {0}{1}\n".format(game.non_predictor.left, game.non_predictor.right))

                game.validate()
            else:
                game.predictor.random_hands()
                game.predictor.random_shout()
                print("\nAI is the predictor, what is your input?\n")
                
                left, right = get_input()
                game.non_predictor.set_hands(left, right)
                print("\n{0}{1}\n".format(game.predictor.left, game.predictor.right))
                

                print("AI: {0}{1}{2}\n".format(game.predictor.left, game.predictor.right, game.predictor.guess))

                game.validate()
        else:
            con = input("\nDo you want to play again?\n")
            if(con.upper() == "Y"):
                continue_flag = True
                game.ending = False
            elif(con.upper() == "N"):
                continue_flag = False
            print("")

if __name__ == '__main__':
    main()