# import tank class file
from tankClass import Tank

# create tank object
tank = Tank()

# move the tank forward for 2.5 seconds & stop
tank.forward(2.5)
tank.stop(2)

# turn the tank to the left & stop 
tank.turnleft()
tank.stop(2)

# move the tank forward for 2.1 seconds & stop
tank.forward(2.1)
tank.stop(2)

# move the tank backwards for 4 seconds & stop
tank.backward(4)
tank.stop(2)


