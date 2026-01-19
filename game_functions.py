import random
import math
# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    # values_num = len(poss_values)
    # if values_num > 1:
    #     if values_num % 2 == 0:
    #         value = poss_values[values_num/2]
        
    #     else:
    #         pre_val = math.ceil(values_num/2)
    #         print(pre_val)
    #         value = poss_values[pre_val]
        
    # return(value)

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
    split_word = list(word)
    for i in range(len(split_word)):
        if split_word[i] == letter:
            board.insert(i, letter)
            taken_out = board.pop(i+1)
            letter_found = True

    if letter_found == True:
        print("Well done!  '", letter, "' is in the word")
        return(True)

    if letter_found == False:
        print("Sorry '", letter, "' is not in the word")
        return(False)
