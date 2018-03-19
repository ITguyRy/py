import random

cpu = random.randint(1,101)

low = 1 # starting off with 0 - 100 range of guess
num = 101
count = 0 # count variable to count how many tries the cpu will take to guess
human = int(input("What is your number human? \n"))
while True:
    try:
        count += 1
        cpu = random.randint(low,num)
        if (human > cpu):
            low = cpu

        elif (human < cpu):
            num = cpu

        elif (human == cpu):
            print("you guessed the right number")
            print(cpu)
            print("I took {} tries to figure out your number.".format(count))
            break

        else:
            continue

        print(cpu)
    except ValueError:
        print("ops")
