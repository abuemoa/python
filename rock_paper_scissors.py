import random

end_of_game = ""
def is_win(player, opponent):
    if (player == 'r' and opponent == 's' or player == 'p' and opponent == 'r' or player == 's'\
        and opponent == 'p'):
        return True 

while end_of_game == "y" or end_of_game == "":
    def play():
        user = input("'r' for rock, 'p' for paper and 's' for scissors:\n")
        computer = random.choice(['r', 'p', 's'])

        if user == computer:
            return "It's a tie"
        elif is_win(user,computer):
            return "you won"
    print(play())
    end_of_game = input("If you don't want to continue playing this game, press the button 'n'\n")
    if end_of_game == "y" or end_of_game == "Y":
        end_of_game = "y"
    elif end_of_game == "n" or end_of_game == "N": 
        end_of_game = "n"
    else:
        end_of_game = "y"
        


