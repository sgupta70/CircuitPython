##Sahana Gupta
##DistanceSensor 
##this code will madke the LED change colors depending on the distance from the sensor

import board
import time 
import neopixel
import adafruit_hcsr04
import simpleio
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.1



while True:

    try:
        distance = sonar.distance
        (print (distance))
    except RuntimeError:
        print("Retrying!")
        r = 0 
        b = 0 
        g = 255
        time.sleep(0.1)

    if distance < 5:
        r = 255
        g = 0 
        b = 0 
        r = int(r) 
        g = int(g)
        b = int(b)
        print("<5")
    elif distance > 5 and distance < 20:
        r = 0
        b = 0
        g = 255
        r = int(r) 
        g = int(g)
        b = int(b)
        print(">5<20")
    elif distance > 20: 
        r = 0 
        g = 0 
        b = 255 
        r = int(r) 
        g = int(g)
        b = int(b)
        print(">20")

    
    

    print (r,g,b)
    dot.fill((r,g,b))
    time.sleep (0.05)