from milestone_2 import word_list
from milestone_3 import guess

def check_guess(guess):
    return guess 
     
def ask_for_inpput():
    guess_num = 0
    guess = input("guess a letter: ").upper()
    check_guess(guess)
    if check_guess(guess) == True:
        return True
    elif guess_num == 3:
        return False
    else:
        guess_num += 1
ask_for_inpput()



