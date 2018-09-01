#!/usr/bin/python
# created by STCDEV001 & ANDNIC019, 01/09/2018

import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

# init variables & constants
GPIO.setmode(GPIO.BCM) # use GPIO pin numbering
delay = 300 # button debounce time

# set pin names
resetpin = 19
freqpin = 16
stoppin = 20
displaypin = 21

# setup pin modes
GPIO.setup(resetpin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(freqpin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(stoppin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(displaypin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#try-finally block to handle GPIO cleanup and robust termination
try:
    #loop for programme execution    
    while True: # make the code run until an exception is thrown
        foo = 0 #for use with empty programme loop (pure button control)
        
finally:
    GPIO.cleanup()