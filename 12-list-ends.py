
# import random module to create a random list
import random


# generate a random set of numbers in a list
def get_list():
    old_list = random.sample(range(100),5)
    return old_list

# slice the first number and the last number in the list
def create_list(old_list):
    return old_list[0], old_list[-1]


# main function that wraps everything together. Prints out first random list for validation and first and last numbers.
def main():
    old_list = get_list()
    print(old_list)
    new_list = create_list(old_list)

    print(new_list)


# execute main
main()
