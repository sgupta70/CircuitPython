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
For this assignment we were required to use the HC-SR04 sensor to measure the distance from an object, depending on the distance the LED would change colors going through the colors from red to green to blue. 

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
![ezgif com-gif-maker](https://user-images.githubusercontent.com/71349797/134724959-4f1d69a2-bb28-4c98-8dd7-6bff58e07b80.gif)

Image Credit does to [Gabbi D](https://github.com/gdaless20/Circuitpython)

### Wiring
![Screenshot (3)](https://user-images.githubusercontent.com/71406903/192614570-c0fe8ff7-9f1b-4d20-8237-f645cfd45fa3.png)
### Reflection
In this assignment I first had to get my HC-SR04 sensor to calculate the distance from an object, then I added on using some code from the Hello_CircuitPython assignment to turn on the LED, and finally using a map function the LED would go through all the colors. IN the beginning I wasn't sure how to do this assignment 




## CircuitPython_LCD

### Description & Code
For this assignment we had to use our LCD screen as an output and have two inputs such as buttons. Every time one of the buttons is pushed the LCD starts counting up, when the other button is pushed it starts counting down. 
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
![LCD](https://drive.google.com/file/d/1r9t-RCMkPbK9uwj-muDTGOO9x-UGuBon/view?usp=sharing)
### Wiring
![Screenshot (7)](https://user-images.githubusercontent.com/71406903/192619545-b9e1aba2-fb2a-42be-97bb-c61d9734c652.png)

### Reflection
