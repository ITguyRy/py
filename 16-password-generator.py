import random, string

def password_strength():
    strength = int(input('how strong do you want your password to be? (weak, medium, high)'))


    return strength

def password_gen(strength):

    strength = password_strength()

    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation

    print (''.join((random.choice(chars)) for x in range(strength)))


def main():
    strength = password_strength()

    password_gen(strength)


main()
