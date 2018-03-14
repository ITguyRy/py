import random
#popular variables
userWins = "You won!"
userLose = "You lost!"
cpWin = "Opponent won!"
rock = ''
paper =''
scissor = ''
space = ''




#while loop
while True:
    #Random generated range translated to RPS
    CP = random.randrange(1,4)
    if (CP == 1):
        CP = 'paper'
    elif (CP == 2):
        CP = 'scissors'
    else :
        CP = 'rock'


    #User input RPS
    user = input("Choose rock, paper, or scissors: ")
    print(user)

    # RPS winning code
    if (user == 'exit'):
        break
    elif (user == 'scissors' and CP == 'paper'):
        print(userWins)
    elif (user =='paper' and CP == 'rock'):
        print(userWins)
    elif (user == 'rock' and CP == 'scissors'):
        print(userWins)
    elif (user == CP):
        print('Draw! ')
    else:
        print(cpWin)

    print("Opponent chose: " + str(CP))
    print (space)
