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


![spinningMetro_Optimized](https://user-images.githubusercontent.com/54641488/192549584-18285130-2e3b-4631-8005-0792c2942f73.gif)


And here is how you should give image credit to someone, if you use their work:

Image credit goes to [Rick A](https://www.youtube.com/watch?v=dQw4w9WgXcQ&scrlybrkr=8931d0bc)



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




## CircuitPython_LCD

### Description & Code

```python
Code goes here

```

### Evidence

Pictures / Gifs of your work should go here.  You need to communicate what your thing does.

### Wiring

### Reflection





## NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection
