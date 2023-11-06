from time import sleep
import board
from adafruit_motorkit import MotorKit


class Tank:
    def __init__(self):
        self.kit = MotorKit(0x40)

    
    def forward(self, time, speed1=0.752, speed2=0.652):
        self.kit.motor1.throttle = speed1
        self.kit.motor2.throttle = speed2
        sleep(time)


    def leftturn(self, time=0.71, speed1=0.6, speed2=0.75):
        self.kit.motor1.throttle = speed1
        self.kit.motor2.throttle = speed2
        sleep(time)

    
    def leftturn(self, time=0.71, speed1=-0.6, speed2=-0.75):
        self.kit.motor1.throttle = speed1
        self.kit.motor2.throttle = speed2
        sleep(time)


    def stop(self, time):
        self.kit.motor1.throttle = 0
        self.kit.motor2.throttle = 0
        sleep(time)

