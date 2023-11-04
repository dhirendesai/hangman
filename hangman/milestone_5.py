from milestone_2 import word_list
import random
class Hangman:

    def __init__(self, word_list, num_lives):
        self.word_list = word_list
        self.num_lives = 5
         
word_guessed = random.choice(word_list)
print(word_guessed)

display = []

for letter in word_guessed:
    display += '_'
print(display)
print(word_guessed)


