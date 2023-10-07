from time import sleep

import OPi.GPIO as GPIO


class Tank:
    def __init__(self):
        GPIO.setmode(GPIO.SUNXI)

        self.motor1fwd = 'PA7'
        self.motor1rev = 'PA8'
        self.motor2fwd = 'PA9'
        self.motor2rev = 'PA10'
        self.fwdmotor = [self.motor1fwd, self.motor2fwd]
        self.revmotor = [self.motor1rev, self.motor2rev]

        GPIO.setup(self.motor1fwd, GPIO.OUT)
        GPIO.setup(self.motor2fwd, GPIO.OUT)

    def forward(self, time):
        GPIO.output(self.fwdmotor, GPIO.HIGH)
        sleep(time)

    def stop(self):
        GPIO.output(self.fwdmotor, GPIO.LOW)
        GPIO.output(self.revmotor, GPIO.LOW)
