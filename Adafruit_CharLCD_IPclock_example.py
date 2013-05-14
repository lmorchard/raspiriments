#!/usr/bin/python

from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import * 
from time import sleep, strftime
from datetime import datetime
from ShiftOutputGPIO import ShiftOutputGPIO
import RPi.GPIO as GPIO

shift_out = ShiftOutputGPIO(num_channels=8)

counters = [0, 0, 0, 0]
counter_pins = [22, 27, 17, 4]

def button_callback(chan):
    try:
        pos = counter_pins.index(chan)
        counters[pos] += 1
    except ValueError, e:
        pass
    
for pin in counter_pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(pin, GPIO.RISING)
    GPIO.add_event_callback(pin, button_callback)


lcd = Adafruit_CharLCD(pin_rs=4, pin_e=5, pins_db=[0,1,2,3], GPIO=shift_out)

cmd = "ip addr show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1"

lcd.begin(16,1)

def run_cmd(cmd):
        p = Popen(cmd, shell=True, stdout=PIPE)
        output = p.communicate()[0]
        return output

while 1:
    lcd.clear()
    ipaddr = run_cmd(cmd)
    lcd.message("\n".join([
        "Hello world! :)",
        '%s' % counters,
        datetime.now().strftime('%b %d  %H:%M:%S'),
        'IP %s' % ( ipaddr ),
    ]))
    sleep(1)