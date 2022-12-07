import random
import string 

precipitation = ("Rain", "Drizzle", "Ice Pellets", "Hail", "Small Hail", "Snow", "Snow Grains", "Ice Crystals")
with open("parks.csv", "w") as file:
    statenames = open("parknames.csv","r")
    i = 1
    for line in statenames:
        parkname = line.split(",")[0]
        state = line.split(",")[1]
        mintemp = random.randrange(-50,50)
        maxtemp = random.randrange(mintemp,120)
        calendar = (''.join(random.choice(string.ascii_lowercase) for i in range(10)))
        file.write(str(i) +"_ " + parkname + "_ " + str(random.randrange(1,67)) + "_ " + str(i) + "_ " + calendar + ".com" +"_ "+ str(mintemp) + ", " + str(maxtemp) + "_ " +  random.choice(precipitation) +"_ " +  (str(random.randrange(34,40)+random.random()) + ", " + str(random.randrange(74,118)+random.random()))  + "\n")
        i+=1