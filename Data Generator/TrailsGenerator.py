import random
import string

terrain = ["Hill", "Mountainous", "Alpine Tundra", "Plateau", "Valley", "Canyon", "Forest", "Desert", "Dunes", "Marsh"]
with open("trails.csv", "w") as file:
    for i in range(1,10001):
        file.write((''.join(random.choice(string.ascii_lowercase) for i in range(10))) + "_ " + str(random.randrange(1,62)) + "_ " + str(random.randrange(1,5)) + "_ " + random.choice(terrain) + "_ " + random.choice(['0','1']) + "_ " + str(random.randrange(1,1000)) + "\n")
        i+=1        