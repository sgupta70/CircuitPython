## Sahana Gupta 
## CircuitPython LCD
##

import board
import time
from digitalio import DigitalInOut, Direction, Pull
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface


btn = DigitalInOut(board.D7)
btn.direction = Direction.INPUT
btn.pull = Pull.UP


# get and i2c object
i2c = board.I2C()
# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x3f), num_rows=2, num_cols=16)
lcd.print("Hello, Engineer!")
time.sleep(2)
lcd.clear()

while True:
    if not btn.value:
        lcd.set_cursor_pos(0,0)
        lcd.print("BTN is down")
    else:
        lcd.set_cursor_pos(0,0)
        lcd.print("BTN is up  ")
        pass

    time.sleep(0.1) # sleep for debounce