import random

with open("visitorcenters.csv", "w") as file:
    for i in range(1,62):
        file.write(str(i) + "_ " + str(random.randrange(0,20)) + "_ " + str(random.randrange(0,2)) + "_ " + str(random.randrange(4,8)) + ", "+ str(random.randrange(20,24)) + "_ " + str(i) + "\n")
        i+=1