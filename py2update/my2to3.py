#!/usr/bin/python3

thisround = 0
while(True):
    print('wht is the ipv4 address used to broadcast on local network? ')
    answer = input()
    thisround = thisround + 1
    if (answer == '255.255.255.255'):
        print('correct!')
        break
    elif (thisround == 3):
        print('sorry, the anser was 255.255.255.255')
        break
    else: 
        print('sorry try again!')


