#!/usr/bin/python

from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import * 
from time import sleep, strftime
from datetime import datetime
from ShiftOutputGPIO import ShiftOutputGPIO

shift_out = ShiftOutputGPIO()
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
	lcd.message(datetime.now().strftime('%b %d  %H:%M:%S\n'))
	lcd.message('IP %s' % ( ipaddr ) )
	sleep(2)
