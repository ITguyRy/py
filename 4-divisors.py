

# I had to look up solution. I forgot to define a list to range. which gave me traceback error.
# time took 10 minutes.

num = int(input("Provide a number to find divisable numbers:\n"))


x = list(range(1,num+1))

a = []

for i in x:
    if (num % i == 0):

        a.append(i)

print(a)
