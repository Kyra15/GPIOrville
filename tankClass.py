from time import sleep
import board
from adafruit_motorkit import MotorKit


class Tank:
    def __init__(self):
        self.kit = MotorKit(i2c=board.I2C(), pwm_frequency=speed)

    def forward(self, time, speed1, speed2):
        self.kit.motor1.throttle = speed1
        self.kit.motor2.throttle = speed2
        sleep(time)


    def stop(self):
        self.kit.motor1.throttle = 0
