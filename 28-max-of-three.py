

def user_in():
    x = int(input("provide a number: \n"))
    return x




def max_compute():
    a = user_in()
    b = user_in()
    c = user_in()

    if a > b and a > c:
        print("Your biggest number is {}".format(a))
    elif b > a and  b > c:
        print("Your biggest number is {}".format(b))
    elif c > b and c > a:
        print("Your biggest number is {}".format(c))
    elif a == b and b > c:
        print("Your biggest number {} was inputted twice!".format(b))
    elif b == c and b > a:
        print("Your biggest number {} was inputted twice!".format(b))
    elif a == c and a > b:
        print("Your biggest number {} was inputted twice!".format(a))
    elif a == b and b == c :
        print("your numbers are equal")

max_compute()
