import random

word_list = []
with open('sowpods.txt', 'r') as pods:
    pod = pods.readline().strip()
    while pod:
        pod = pods.readline().strip()
        word_list.append(pod)

#word_list = " ".join(word_list)

num = random.randint(0,len(word_list))

#print(type(word_list))

print(word_list[num])
