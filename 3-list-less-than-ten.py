
x = []
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


n = int(input("Let's check the list for numbers smaller than what you tell me: "))

for i in a:
    if i < n:
        x.append(i)


print(x)
