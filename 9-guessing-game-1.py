import random

rand_num = random.randrange(1,10)

high = "that number is too high!"
low = "that number is too low!"
bullseye = "you guessed it!"

while True:
    try:
        guess = int(input("Guess the number. I'll tell you if it's too high or low.\n"))

        if (guess > rand_num):
            print(high)
        elif(guess < rand_num):
            print(low)
        elif(str(guess) == "exit"):
            break
        else:
            print(bullseye)
            rand_num = random.randrange(1,10)

    except ValueError, TypeError:
        break
