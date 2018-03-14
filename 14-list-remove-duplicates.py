import random


def generate_list():

    randoms = random.sample(range(10),10)
    x = []

    for i in randoms:
        if (i not in x ):
            x.append(i)
    return x

def main():

    x = generate_list()
    print(x)


main()
