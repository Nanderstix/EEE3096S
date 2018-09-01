#!/usr/bin/python
# created by STCDEV001 & ANDNIC019, 01/09/2018

import RPi.GPIO as GPIO
import time
import Adafruit_MCP3008
import os
GPIO.setwarnings(False)

# init variables & constants
GPIO.setmode(GPIO.BCM) # use GPIO pin numbering
delay = 300 # button debounce time
lightmax = 898 # maximum expected LDR value

# set pin names
resetpin = 19
freqpin = 16
stoppin = 20
displaypin = 21
CLK = 11
MISO = 9
MOSI = 10
CS = 8

# setup pin modes
GPIO.setup(resetpin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(freqpin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(stoppin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(displaypin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(MOSI, GPIO.OUT)
GPIO.setup(MISO, GPIO.IN)
GPIO.setup(CLK, GPIO.OUT)
GPIO.setup(CS, GPIO.OUT)

mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, mosi=MOSI, miso=MISO)

#try-finally block to handle GPIO cleanup and robust termination
try:
    # print header line
    print ("Time \t Timer \t Pot \t Temp \t Light")
    
    #loop for programme execution    
    while True: # make the code run until an exception is thrown
        #foo = 0 #for use with empty programme loop (pure button control)
        
        # read MCP raw input values
        tempraw = mcp.read_adc(0)
        lightraw = mcp.read_adc(1)
        potraw = mcp.read_adc(2)
        
        # convert raw values to meaningful output numbers
        actualtime = 0
        timer = 0
        tempvolt = 3.3*(tempraw/1023)# convert raw value to voltage for use in formula
        temp = (tempvolt-0.5)/(0.01)
        light = 100*(lightraw/lightmax)
        pot = 3.3*(potraw/1023)
        
        # Display values
        print ("%d \t %d \t %.1f V \t %.0f C \t %.0f%%" % (actualtime, timer, pot, temp, light))
        time.sleep(0.5) # delay for a half second
        
finally:
    GPIO.cleanup()