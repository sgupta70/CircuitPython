#Sahana Gupta 
#Hello CircuitPython
# this code makes the LED light on the arduino turn on to a color of our choice 

import board
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.1


print("Make it blue!")

while True:
    dot.fill((255, 51, 153))