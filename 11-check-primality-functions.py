
def num_input():
    num = int(input('Give me a number to check if it is prime:\n'))
    return num

def check(num):

    if (num % 2 != 0):
        print('that number is a prime number')
    else:
        print('that number is not a prime number')


def __main__():
    num = num_input()
    check(num)



__main__()
