#!/usr/bin/python3

round = 0
while(True):
    round = round + 1
    print('finish the movie title, "monty python\'s the life of ------"')
    answer = input()
    answer = answer.lower()

    if (answer == 'Brian'):
        print('Correct')
        break
    elif (answer == 'SHURBBURY'):
        print('secret answer')
    elif (round == 3):
         print('Sorry, the answer was Brian.')
         break
    else: 
        print('sorry! try again!')

