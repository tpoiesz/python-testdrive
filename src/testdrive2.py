import random

high_number = 20
low_number = 1
keep_playing = True
message = 'Enter a number between ' + str(low_number) +\
    ' and ' + str(high_number) + ': '

while keep_playing:
    chosen = random.randint(low_number, high_number)
    guessed = False
    while not guessed:
        guess = int(input(message))
        if guess < chosen:
            print("Too low!")
        elif guess > chosen:
            print("Too high!")
        else:
            print("Good job!")
            guessed = True

    keep_playing = input("Would you like to play again?") == "yes"
