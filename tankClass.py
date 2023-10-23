from time import sleep

import RPi.GPIO as GPIO


class Tank:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)

        self.motor1fwd = 21
        self.motor1rev = 22
        self.motor2fwd = 23
        self.motor2rev = 24 #pwm pin
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
