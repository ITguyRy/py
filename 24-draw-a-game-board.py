
num = user_in("How many Columns? \n")

def user_in(x):
    x = int(input(x))
    return x

def model(num, shape):
    print(shape*num)

def sides(num,shape):
    print(shape*(num + 1))


def column(model, sides):
    count = 0
    ask = user_in("How many rows? \n")
    while count < ask:
        count += 1
        w = model(num, ' ---')
        l = sides(num, '|   ')
    w = model(num, ' ---')

column(model, sides)
