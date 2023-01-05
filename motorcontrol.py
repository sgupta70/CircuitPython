
import time
import board
import digitalio
import pwmio
import simpleio
from adafruit_motor import motor

button = digitalio.DigitalInOut(board.GP20)
button.direction = digitalio.Direction.INPUT

buzzer = board.GP22

PWM_M1A = board.GP4  # pick any pwm pins on their own channels
PWM_M1B = board.GP5

# DC motor setup
# DC Motors generate electrical noise when running that can reset the microcontroller in extreme
# cases. A capacitor can be used to help prevent this.
pwm_1a = pwmio.PWMOut(PWM_M1A, frequency=10000)
pwm_1b = pwmio.PWMOut(PWM_M1B, frequency=10000)
motor1 = motor.DCMotor(pwm_1a, pwm_1b)

NOTE_C4 = 261
NOTE_G4 = 392

print()
print("***DC motor test***")
print("Press on-board button (GP20)")

simpleio.tone(buzzer, NOTE_C4, duration=0.1)
simpleio.tone(buzzer, NOTE_G4, duration=0.15)

speed = 0

while True:

    if button.value == False:
        simpleio.tone(buzzer, NOTE_C4, duration=0.1)

        while speed < 1:
            print("Motor speed: {}".format(speed))
            motor1.throttle = speed
            speed += 0.01
            time.sleep(0.05)

        speed = 1
        while speed > -1:
            print("Motor speed: {}".format(speed))
            motor1.throttle = speed
            speed -= 0.01
            time.sleep(0.05)

        speed = -1
        while speed < 0:
            print("Motor speed: {}".format(speed))
            motor1.throttle = speed
            speed += 0.01
            time.sleep(0.05)

        motor1.throttle = 0