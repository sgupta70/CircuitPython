##Sahana Gupta
##DistanceSensor 
##this code will madke the LED change colors depending on the distance from the sensor

import board
import time 
import neopixel
import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.1



while True:
   distance = sonar.distance
   (print (distance))
     if distance < 5:
    r = 255
    g = 0 
    b = 0 
    elif distance > 5:



    elif distance > 20: 
        r = 0 
        g = 0 
        b = 255 

    dot.fill((255, 51, 153))
    try:
        print((sonar.distance,))
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)