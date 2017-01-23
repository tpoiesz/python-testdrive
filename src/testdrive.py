import random

roll = True

while roll:
    print(random.randrange(1, 6))
    roll = input('Would you like to roll the dice again?(yes/no)') == 'yes'
