import milestone_2

guess = input('enter a letter ')

guess = guess.isalpha()

while guess == guess:
       
       print('Good guess')

       break

else:
    print('Invalid letter, enter a single alphabetical character ')

if guess in milestone_2.word_list:
      print(f'good guess {guess}')

else:
      print(f'{guess} is not in the list')