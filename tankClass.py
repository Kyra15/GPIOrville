from time import sleep
import board
from adafruit_motorkit import MotorKit


class Tank:
    def __init__(self, speed):
        self.speed = speed
        self.kit = MotorKit(i2c=board.I2C(), pwm_frequency=speed)

    def forward(self, time):
        self.kit.motor1.throttle = 1.0
        sleep(time)


    def stop(self):
        self.kit.motor1.throttle = 0
