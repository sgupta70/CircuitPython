# CircuitPython

## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
---

## Hello_CircuitPython

### Description & Code
For this assignment we were assigned to make the neopixel on our metro express turn blue. 

```
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

```


### Evidence


[neopixel](https://user-images.githubusercontent.com/71406903/192611881-611d45dc-92f3-4ed2-b3b6-a9de7280dc50.jpg)



### Wiring
There were no wires needed for this project, just the Metro Express. 

### Reflection
This was the first assignment using CircuitPython and in the beginning I was a little unsure. 




## CircuitPython_Servo

### Description & Code
In this assignment we had to 
```
#Sahana Gupta
#CircuitPython Servo 
#This code will turn on a motor and make it rotate 180 degrees back and forth

"""CircuitPython Essentials Servo standard servo example"""
import time 
import board 
import pwmio
from adafruit_motor import servo


pwm = pwmio.PWMOut(board.D3, duty_cycle=2 ** 15, frequency=50) #using the PWMOut function within the pwmio library 


my_servo = servo.Servo(pwm)

while True:
    for angle in range(0, 180, 5): #the servo rotates 180 degrees 
        my_servo.angle = angle
        time.sleep(0.05) #pauses for 0.05 seconds
    for angle in range(180, 0, -5): #the servo rotates 180 degrees ther other way 
        time.sleep(0.05) #pauses for 0.05 seconds

```

### Evidence

Pictures / Gifs of your work should go here.  You need to communicate what your thing does.

### Wiring

### Reflection




## CircuitPython_DistanceSensor

### Description & Code

```
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
    elif distance < 25 and distance > 20: ## if the distance is greater than 5cm and less than 20cm the led goes from red to blue  
        r = int(simpleio.map_range(distance 5, 20, 255, 0))
        g = int(0)
        b = int(simpleio.map_range(distance 5, 20, 0, 255))
        print(">5<20")
    elif distance < 20 and distance > 35: ## if the distance is greater than 20cm and less than 30cm the led goes from blue to green 
        r = int(0)
        g = int(simpleio.map_range(distance 20, 35, 0, 255))
        b = int(simpleio.map_range(distance 20, 35, 255, 0))
        print(">20<35")
    elif distance > 35: ## if the distance is greater than 35cm the led is green 
        r = 0 
        g = 255
        b = 0
        print(">35")

    
    

    print (r,g,b)
    dot.fill((r,g,b))
    time.sleep (0.05)

```

### Evidence

Pictures / Gifs of your work should go here.  You need to communicate what your thing does.

### Wiring

### Reflection





## CircuitPython_LCD

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection
