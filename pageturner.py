
import time
import board
import pwmio
from adafruit_motor import servo
from digitalio import DigitalInOut, Direction, Pull

btn1 = DigitalInOut(board.D11)
btn1.direction = Direction.INPUT
btn1.pull = Pull.DOWN

btn2 = DigitalInOut(board.D12)
btn2.direction = Direction.INPUT
btn2.pull = Pull.DOWN 

# create a PWMOut object on Pin A2.
pwm1 = pwmio.PWMOut(board.D10, duty_cycle=2 ** 15, frequency=50)
pwm2 = pwmio.PWMOut(board.D9, duty_cycle=2 ** 15, frequency=50)
pwm3 = pwmio.PWMOut(board.D8, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.

large_servo = servo.Servo(pwm1)
small_servo = servo.Servo(pwm2) 
#arm_servo = servo.Servo(pwm3, min_pulse=600, max_pulse=2700)

#set servoes to starting position
    #arm servo to UP
    #lg servo to STOP
    #sm servo to .... right? 180?

large_servo.angle = 0
time.sleep(1)
large_servo.angle = 180
angle = 90 

while True:

    #this is just the UP example. copy and flip values for DOWN
    # If button is pressed
    if btn1.value:
        print ("btn1 pressed")

    # is the sm servo in the correct position?

    # Drop lg servo
        #We will write code for "arm servo" to move lg servo, here.
    # Rotate Lg servo for # seconds7

        large_servo.angle = 180 
        time.sleep(1)
        print("largego")
        large_servo.angle = 90 
        print("largestop")
    #wait 0.x seconds to allow page to "Settle"
        time.sleep(1)
    # move Sm servo
        small_servo.angle = 90
        print("smallgo")
        time.sleep(1)
        small_servo.angle = 0
        print("smallDone")
        time.sleep(1)
    # Lift Lg servo and Sm servo reset
        #We will write code for "arm servo" to move lg servo, here.