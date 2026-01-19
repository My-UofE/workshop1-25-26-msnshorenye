import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    x = random.choice(poss_values)   
    return x

# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val, next_val, user_input):
    if user_input == "h":
        if current_val < next_val:
            return True
        
        else:
            return False
    
    if user_input == "l":
        if current_val > next_val:
            return True
        else:
            return False

# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    letter_found = False
    for i in (0, len(word)):
        if word[i] == letter:
            board[i] == letter
            letter_found = True

    if letter_found == True:
        print("Well done!  '", letter, "' is in the word")
        return(True)

    if letter_found == False:
        print("Sorry '", letter, "' is not in the word")
        return(False)
