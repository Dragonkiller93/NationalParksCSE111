import random

climates = ["Alpine" , "Desert" , "Humid continental" , "Humid subtropical" , "Ice cap" , "Oceanic" , "Subarctic" , "Semi arid" , "Mediterranean" , "Tropical monsoon" , "Tropical rainforest" , "Tropical savanna" , "Tundra" , "Polar" ]
with open("statetable", "w") as file:
    statenames = open("statenamelist.txt","r")
    i = 1
    for name in statenames:
        file.write(str(i) + ", " + (str(random.randrange(34,40)+random.random()) + "-" + str(random.randrange(74,118)+random.random())) + ", " + str(random.randrange(-11,12)) + ", " + random.choice(climates)+", "+ name + "\n")
        i+=1


        