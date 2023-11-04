import random
word_list = ['apple', 'banana', 'mango', 'kiwi', 'grapes']
num_lives = 5
print(word_list)

choice = random.choice(word_list)
print(choice)

display=[]

for i in range (len(choice)): 
    display += '_'

print(display)

game_over=False

while not game_over:    
    gussed_letter=input("Gusse a letter").lower()

    for position in range(len(choice)):
        letter = choice[position]
        if letter == gussed_letter:
            display[position] = gussed_letter
    print(display)

if gussed_letter not in choice:
    num_lives -=1

    if num_lives == 0:
        game_over = True
        print('You died, Game over!')
if '_' not in display:
    game_over = True
    print('You have won the game')