# import time for delays
from time import sleep

# import the raspberrypi gpio library
import RPi.GPIO as GPIO


# create the tank class
class Tank:
    # when the program start, set the gpio mode to bcm so you can use numbers for pins
    def __init__(self):
        GPIO.setmode(GPIO.BCM)

        # set pin numbers for each wire (these are approximations and will be update once we get the robot working)
        self.motor1fwd = 21
        self.motor1rev = 22
        self.motor2fwd = 23
        self.motor2rev = 24 #pwm pin
        self.fwdmotor = [self.motor1fwd, self.motor2fwd]
        self.revmotor = [self.motor1rev, self.motor2rev]

        # set up the motors as outputs
        GPIO.setup(self.motor1fwd, GPIO.OUT)
        GPIO.setup(self.motor2fwd, GPIO.OUT)

    # define the forward function, which outputs high to the forward motors for as much time as is inputted
    def forward(self, time):
        GPIO.output(self.fwdmotor, GPIO.HIGH)
        sleep(time)

    # define the stop function, which just sets the output for all motors to low.
    def stop(self):
        GPIO.output(self.fwdmotor, GPIO.LOW)
        GPIO.output(self.revmotor, GPIO.LOW)
