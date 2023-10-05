from gpiozero import *
from time import sleep

motorL = Motor(21, 22)
motorR = Motor(23, 24)

motorL.forward(0.6)
motorR.forward(0.6)

sleep(2)

motorL.stop()
motorR.stop()

