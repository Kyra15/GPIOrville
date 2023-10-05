from time import sleep

import OPi.GPIO as GPIO

GPIO.setmode(GPIO.SUNXI)

motor1fwd = 'PA7'
motor1rev = 'PA8'
motor2fwd = 'PA9'
motor2rev = 'PA10'

fwdmotor = [motor1fwd, motor2fwd]
revmotor = [motor1rev, motor2rev]

GPIO.setup(motor1fwd, GPIO.OUT)
GPIO.setup(motor2fwd, GPIO.OUT)

print("Finished Setup")
GPIO.output(fwdmotor, GPIO.HIGH)

sleep(2)

print("Finished FwdMotors")

GPIO.output(fwdmotor, GPIO.LOW)
GPIO.output(revmotor, GPIO.LOW)

print("Done")

