import random
word_list = ['apple', 'banana', 'mango', 'kiwi', 'grapes']
print(word_list)

choice = random.choice(word_list)
print(choice)

guess = input('Enter a single letter')
print(guess.isalpha())

if len(guess) == 1:
    print('Good guess')

else:
    print('Opps! That is not a valid input')