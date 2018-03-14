#Simple program to reverse user inputted sentence.

#function simply to receieve user input.
def get_sentence():
    name = input('Give me a sentence to reverse: \n')
    return name


#reverse function
def reverse_engine(name):
    #local defined variables
    count = 0
    rev = 0

    # defined an empty list to append strings to.
    reverse_list = []
    #split the initial sentence given by the user so it becomes a list.
    result = name.split()
    #record the length of the sentence
    length = len(result)

    #while loop to start a count loop from the last word of the sentence to the first
    while (length  > count): # As long as the length is still greater than count keep looping
        count+=1 # count variable keeps the loop going
        rev-=1 #rev variable starts from the last value in the list to the first

        reverse_list.append(result[rev]) #append to the empty list

        #print(result[rev]) # only for testing


    final_result = " ".join(reverse_list) # join the strings in the list together, to form a sentence again instead of the list.
    print (final_result) # prints final result

#main function to wrap it all together
def main():
    name = get_sentence()
    reverse_engine(name)

main()
