with open('sowpods.txt', 'r') as pods:
    pod = pods.readline()
    #pod = pods.read() reads all
    while pod:
        print(pod) # reads all with linebreak
        pod = pods.readline()


print(pod)
