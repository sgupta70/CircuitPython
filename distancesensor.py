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
        time.sleep(0.1)

    if distance < 5: ## if distance is less than 5cm then the light will turn red
        r = 255
        g = 0 
        b = 0 
        print("<5")
    elif distance < 20: ## if the distance is greater than 5cm and less than 20cm then the light turns green 
        r = 0
        b = 0
        g = 255
        r = int(r) 
        g = int(g)
        b = int(b)
        print(">5<20")
    else: ## if the distance is greater than 20cm then the light turns blue 
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