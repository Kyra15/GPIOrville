from time import sleep

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

pwm = GPIO.PWM(24, 200)
pwm.start(50)

motor1fwd = 21
motor1rev = 22
motor2fwd = 23
motor2rev = 24 #pwm pin

fwdmotor = [motor1fwd, motor2fwd]
revmotor = [motor1rev, motor2rev]

GPIO.setup(motor1fwd, GPIO.OUT)
GPIO.setup(motor2fwd, GPIO.OUT)
GPIO.setup(motor1rev, GPIO.OUT)
GPIO.setup(motor2rev, GPIO.OUT)

print("Finished Setup")
GPIO.output(fwdmotor, GPIO.HIGH)

sleep(2)

print("Finished FwdMotors")

GPIO.output(fwdmotor, GPIO.LOW)
GPIO.output(revmotor, GPIO.LOW)
pwm.stop()

print("Done")
