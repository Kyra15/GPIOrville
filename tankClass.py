# import necessary libraries
from time import sleep
from adafruit_motorkit import MotorKit

# create tank class
class Tank:
    # initialize the motor kit library
    def __init__(self):
        self.kit = MotorKit(0x40)

    # define the forward function, which takes parameters time and 2 different speeds for each wheel. If nothing is provided, the default values are used.
    def forward(self, time, speed1=0.775, speed2=0.78):
        self.kit.motor1.throttle = speed1
        self.kit.motor2.throttle = -speed2
        sleep(time)

    # define the leftturn function, which takes parameters time and 2 different speeds for each wheel. The function 
    def leftturn(self, time=0.75, speed1=.765, speed2=0.77):
        self.kit.motor1.throttle = -speed1
        self.kit.motor2.throttle = -speed2
        sleep(time)

    # define the rightturn function, which takes parameters time and 2 different speeds for each wheel
    def rightturn(self, time=0.75, speed1=.765, speed2=0.77):
        self.kit.motor1.throttle = speed1
        self.kit.motor2.throttle = speed2
        sleep(time)

    # define the backward function, which takes parameters time and 2 different speeds for each wheel
    def backward(self, time, speed1=0.775, speed2=0.78):
        self.kit.motor1.throttle = -speed1
        self.kit.motor2.throttle = speed2
        sleep(time)


    def stop(self, time):
        self.kit.motor1.throttle = 0
        self.kit.motor2.throttle = 0
        sleep(time)


    def contineforward(self, speed1=0.775, speed2=0.78):
        self.kit.motor1.throttle = speed1
        self.kit.motor2.throttle = -speed2

