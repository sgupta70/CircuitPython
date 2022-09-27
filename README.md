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
For this assignment we were assigned to learn the new CircuitPython cod and make the neopixel on our Metro Express turn blue. 

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


![neopixel](https://user-images.githubusercontent.com/71406903/192611881-611d45dc-92f3-4ed2-b3b6-a9de7280dc50.jpg)



### Wiring
There were no wires needed for this project, just the Metro Express. 

### Reflection
This was the first assignment using CircuitPython so it was kind of different in the beginning. After getting started I realized that it wasn't that different from arduino. I was able to easily make the light turn on and I was able to change the LED to different colors plugging in the numbers that will make the corresponding color. Overall I enjoyed this assignment and didn't find it difficult. 




## CircuitPython_Servo

### Description & Code
In this assignment we had to get a 180° micro servo to slowly sweep back and forth between 0 and 180°
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


### Wiring
![Screenshot (5)](https://user-images.githubusercontent.com/71406903/192617309-7d16d43c-7788-429a-b7c6-52362cc06706.png)
### Reflection
This assignment 



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
![Screenshot (3)](https://user-images.githubusercontent.com/71406903/192614570-c0fe8ff7-9f1b-4d20-8237-f645cfd45fa3.png)
### Reflection





## CircuitPython_LCD

### Description & Code

```
## Sahana Gupta 
## CircuitPython LCD
##

import board
import time
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from digitalio import DigitalInOut, Direction, Pull

# get and i2c object
i2c = board.I2C()
btn = DigitalInOut(board.D6)
btn2 = DigitalInOut(board.D7)
btn.direction = Direction.INPUT
btn.pull = Pull.UP
btn2.direction = Direction.INPUT
btn2.pull = Pull.UP
# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x3f), num_rows=2, num_cols=16)
cur_state = True
prev_state = True
cur_state2 = True
prev_state2 = True
buttonPress = 0

while True:
    while btn2.value == False:
        cur_state = btn.value
        if cur_state != prev_state:
            if not cur_state:
                buttonPress = buttonPress + 1
                lcd.clear()
                lcd.set_cursor_pos(0,0)
                lcd.print(str(buttonPress))
                time.sleep(0.05)
            else:
                lcd.clear()
                lcd.set_cursor_pos(0,0)
                lcd.print(str(buttonPress))
        prev_state = cur_state
    else:
        cur_state2 = btn.value
        if cur_state2 != prev_state2:
            if not cur_state2:
                buttonPress = buttonPress - 1
                lcd.clear()
                lcd.set_cursor_pos(0,0)
                lcd.print(str(buttonPress))
                time.sleep(0.05)

            else:
                lcd.clear()
                lcd.set_cursor_pos(0,0)
                lcd.print(str(buttonPress))
        prev_state2 = cur_state2

```

### Evidence

### Wiring
![Screenshot (7)](https://user-images.githubusercontent.com/71406903/192619545-b9e1aba2-fb2a-42be-97bb-c61d9734c652.png)

### Reflection
